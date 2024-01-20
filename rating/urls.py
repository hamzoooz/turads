from django.urls import path
from . import views

urlpatterns = [
    
    path('rating/<int:id>', views.rating_item, name='rating_item'),
    # path('users/<int:pk>/rating/', views.rating_user, name='rating_user'),
    # path('user/<str:user>/rating', views.rating_user, name='rating_user'),
    # path('users/<str:username>/rating', views.rating_user, name='rating_user'),
    
]
