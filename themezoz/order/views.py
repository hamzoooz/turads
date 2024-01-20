from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from carts.models import Order, OrderItem


@login_required
def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {"order": order}
    return render(request, 'order/order.html', context)


# templates/order/order.html
@login_required
def orderview(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitem = OrderItem.objects.filter(order=order)
    # print(order)
    # print(orderitem.item.id)
    for item in orderitem:
        print(item.item)
    context = {"order": order, "orderitem": orderitem}

    return render(request, "order/view.html", context)
