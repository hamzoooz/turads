import random
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
import paypalrestsdk
from paypalrestsdk import Payment

from django.urls import reverse
from core.models import Item
from carts.models import Cart,  Order, OrderItem
from users.models import CustomUser 
 
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def create_payment(request):
    carditem = Cart.objects.filter(user=request.user)
    current_user = CustomUser.objects.get(id=request.user.id)
    total_price = 0
    for item in carditem:
        total_price = total_price + item.item.selling_price

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
        },
 
        "transactions": [
            {
                "amount": {
                    "total": total_price,  # Total amount in USD
                    "currency": "USD",
                },
                "description": "Payment for Product || Service from Themezoz.com ",
            }
        ],
    })

    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        # return render(request, 'paypal/payment_failed.html')
        return render(request, 'checkout/checkout.html')

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        
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
        # messages.success(request, " Successfully open your item my order page .")
        # return render(request, 'checkout/checkout.html')
        # return render(request, 'paypal/payment_success.html')
        return redirect("my_order")
    
    else:
        
        messages.error(request, "Tray Again There is error ! ")
        # return render(request, 'paypal/payment_failed.html')
        return redirect("checkout")
 
def payment_failed(request):
    
    messages.error(request, "Tray Again There is error ! ")
    # return render(request, 'paypal/payment_failed.html')
    # return render(request, 'checkout/checkout.html')
    return redirect("checkout")

def payment_checkout(request):
    return render(request, 'checkout/checkout.html')

