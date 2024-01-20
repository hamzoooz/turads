from django.urls import path
from . import views


urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    # number_of_likes
    path('add_like', views.add_like, name='add_like'),
    path('add_dis_like', views.add_dis_like, name='add_dis_like'),
    # path('remove_from_like/', views.remove_from_like, name='remove_from_like'),
]


