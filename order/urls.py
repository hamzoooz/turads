from django.urls import path 
from . import views

urlpatterns = [

    #  Orders
    path('my-orders', views.orders, name='my_order'),
    path('orderview/<t_no>', views.orderview, name='orderview'),

]

