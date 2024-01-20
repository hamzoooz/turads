from django.http.response import JsonResponse
from django.shortcuts import render, redirect
# from carts.models import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from core.models import Item
from carts.models import Cart,  Order, OrderItem
from users.models import CustomUser
import random
from django.conf import settings
from square.client import Client
import hashlib
import uuid
import time
import string

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in carts:
        total_price = total_price + item.item.selling_price
    return render( request, 'carts/cart_view.html', { 'carts': carts, 'total_price': total_price })

# @login_required # get error 
def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            item_id = int(request.POST.get('item_id'))
            item_check = Item.objects.get(id=item_id)
            if (item_check):
                if (Cart.objects.filter(user=request.user.id, item_id=item_id)):
                    return JsonResponse({'status': "Item Already in Cart"})
                else:
                    Cart.objects.create(user=request.user, item_id=item_id)
                    return JsonResponse({'status': "Your item added Successfuly  "})
            else:
                return JsonResponse({'status': "No Such Item Found "})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')


def remove_form_cart(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        if (Cart.objects.filter(user=request.user, item=item_id)):
            cart_item = Cart.objects.get(item=item_id, user=request.user)
            cart_item.delete()
        return JsonResponse({'status': "Your Cart Deleted Successfuly ..."})

# #############################
#          Checkout 
# #############################

@login_required
def checkout(request):
    total_price = 0.0
    carditems = Cart.objects.filter(user=request.user)
    current_user = CustomUser.objects.get(id=request.user.id)
    print(total_price)
    
    for item in carditems:
        print(item.item.selling_price)
        # if item.item.selling_price is not None:
        total_price = total_price + item.item.selling_price
        
    print(total_price)
    
    return render(request, 'checkout/checkout.html', {
        'carditems': carditems,
        'total_price': total_price,
        'current_user': current_user,
    })
    
    
    
    
@login_required(login_url='login')
def placeorder(request):
    # current_user = CustomUser.objects.filter(username=request.user).first()
    # Initialize Square client
    square_client = Client(
    access_token=settings.SQUARE_ACCESS_TOKEN,
    environment='sandbox'  # Change to 'production' for live environment
    )
    
    carditem = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in carditem:
        total_price = total_price + item.item.selling_price
        
    if request.method == "POST":
        
        # Payment amount and currency
        amount_money = {"amount": total_price, "currency": "USD"}  # Adjust amount as needed
        
        # Generate idempotency key
        timestamp = str(int(time.time()))
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        data = f"{timestamp}-{random_string}"
        
        payment_body = {
            # "source_id": request.POST['nonce_from_the_client'],  # Get nonce from client-side
            "amount_money": amount_money,
            "idempotency_key" : hashlib.sha256(data.encode()).hexdigest()
        }

        # Location ID from Square Dashboard
        location_id = settings.SQUARE_LOCATION_ID
        
        try:
            response = square_client.payments.create_payment(location_id, payment_body)
            if response.is_success():
                # Payment successful
                current_user = CustomUser.objects.get(id=request.user.id)
                # check if user data complete to complate 
                if not current_user.first_name:
                    current_user.first_name = request.POST.get('fname')
                    current_user.save()
                if not current_user.last_name:
                    current_user.save()
                    current_user.last_name = request.POST.get('lname')
                    current_user.save()
                if not current_user.email:
                    current_user.email = request.POST.get('email')
                    current_user.save()
                
                # check if user CustomUser data complete to complate 
                if not current_user.phone:
                    current_user.phone = request.POST.get('phone')
                    current_user.save()
                if not current_user.address:
                    current_user.address = request.POST.get('address')
                    current_user.save()
                if not current_user.city:
                    # current_user.city = request.POST.get('city')
                    current_user.save()
                if not current_user.state:
                    current_user.state = request.POST.get('state')
                    current_user.save()
                if not current_user.country:
                    current_user.country = request.POST.get('country')
                    current_user.save()
                if not current_user.pincode:
                    current_user.pincode = request.POST.get('pincode')
                    current_user.save()

                
                new_order = Order()
                new_order.user = request.user
                new_order.fname = request.POST.get('fname')
                new_order.lname = request.POST.get('lname')
                new_order.email = request.POST.get('email')
                new_order.phone = request.POST.get('phone')
                new_order.address = request.POST.get('address')
                new_order.city = request.POST.get('city')
                new_order.state = request.POST.get('state')
                new_order.country = request.POST.get('country')
                new_order.pincode = request.POST.get('pincode')
                new_order.payment_mode = request.POST.get('payment_mode')
                
                # new_order.payment_id = request.POST.get('payment_id')
                card = Cart.objects.filter(user=request.user)
                card_total_price = 0
                
                for item in card:
                    card_total_price = card_total_price + item.item.selling_price 
                    user = item.user.username
                new_order.total_price = card_total_price

                # trackno = "hamzoooz" + str(random.randint(1111111, 9999999))
                trackno = user + str(random.randint(1111111, 9999999))
                while Order.objects.filter(tracking_no=trackno) is None:
                    # trackno = "hamzoooz" + str(random.randint(1111111, 9999999))
                    trackno = user + str(random.randint(1111111, 9999999))
                new_order.tracking_no = trackno
                new_order.save()
                # user, book, create_at, qunatity
                new_order_item = Cart.objects.filter(user=request.user)
                for item in new_order_item:
                    OrderItem.objects.create(
                        order=new_order,
                        price=item.item.selling_price,
                        item=item.item, 
                )
                    order_item = Item.objects.filter(id=item.item_id).first()
                    # order_book.quantity = order_book.quantity - item.book_qty
                    order_item.save()
                    
                # To Clear User's Cart
                Cart.objects.filter(user=request.user).delete()
                messages.success(request, 'Your Order has been placed successfuly ! ')
        
                # payMode = request.POST.get('payment_mode')
                # if (payMode == "Paid by Razorpay"):
                #     return JsonResponse({'status': 'Your Order has been placed successfuly ! '})
                # return JsonResponse({'status': 'Your Order has been placed successfuly ! '})
            else:
                # Payment failed
                return JsonResponse({'status': "Payment Failed: " + response.errors})
                # return HttpResponse("Payment Failed: " + response.errors)
        except Exception as e:
            return JsonResponse({'status': "Payment Error: " +  + str(e)})
 
            # return HttpResponse("Payment Error: " + str(e))

    return redirect('/')

    # return render(request, 'checkout/placeorder.html')
