from django.core.paginator import Paginator
from django.shortcuts import render
from allauth.account.views import LogoutView
from allauth.account.views import SignupView
from django.shortcuts import redirect
from users.models import CustomUser
# from blog.models import  Profile  
from core.models import * 
from django.contrib.auth import login
from carts.models import Cart ,Order , OrderItem 
from wishlist.models import WishList
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
 

items_per_page = 10  # You can adjust this as needed 

# Create your views here.
    # recent_items = Item.objects.order_by('-created_at')
    # paginator = Paginator(recent_items, items_per_page)
    # page_number = request.GET.get('page')
    # items_list = paginator.get_page(page_number)
    # return render(request , 'core/pages/recent-item.html', {
    #     "items_list":items_list,
def user_detail(request , username):
    profile = CustomUser.objects.get(username=username)
    
    items = Item.objects.filter(user=profile)
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    return render(request, 'user/user_details.html',{
        "profile":profile,
        "items_list":items_list,
    })

@login_required
def my_store(request):
    user = request.user
    wishlist  = WishList.objects.filter(user=user)  # Use 'user' instead of 'user_id'
    item_fav = []
    for item in wishlist:
        item_fav.append(item.item)
    favorite  = Item.objects.filter(id__in=wishlist.values('item_id'))  # Use 'user' instead of 'user_id'

    carts_list = Cart.objects.filter(user=user)[0:20]
    # print(carts_list)
    item_cart = []
    for item in carts_list:
        item_cart.append(item.item.id)
    carts = Item.objects.filter(id__in=carts_list.values('item_id'))
 
    order  = Order.objects.filter(user=user)[0:20]
    # order_item  = OrderItem.objects.filter(order=user)[0:20]

    # items = Item.objects.filter(id__in=favorite.values('item_id'))  # Filter items based on 'item_id' in 'MyFav'
    return render(request, 'user/my_store.html', {
        'user': user,
        # 'items': items,
        'favorite': favorite,
        'carts': carts,
        'order': order,
        # 'order_item': order_item,
    })

    
class CustomRegistrationView(SignupView):
    def form_valid(self, form):
        # Call the parent form_valid method to complete the registration.
        response = super().form_valid(form)
        # Log the user in immediately after successful registration.
        login(self.request, self.user )
        return response
    
    

class CustomLogoutView(LogoutView):
    def post(self, *args, **kwargs):
        # Log the user out without confirmation
        response = super().post(self.request, *args, **kwargs)
        return response
    
# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()