from django.urls import path

from . import views 
urlpatterns = [
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('cart/cart_view/', views.cart_view, name='cart_view'),
    path('remove_form_cart', views.remove_form_cart, name='remove_from_cart'),
    
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/placeorder/', views.placeorder, name='placeorder'),
]
# 