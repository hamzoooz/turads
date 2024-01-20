from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from core.models import Item

import uuid

class Cart(models.Model):
    user = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item,  on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    qunatity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.item } - {self.qunatity }"
    
order_status = (
    ('pending', 'pending'),
    ('out for Shipping', 'out for Shipping'),
    ('Completed', 'Completed'), )


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # fname = models.CharField(max_length=150, blank=True, null=False )
    # lname = models.CharField(max_length=150, blank=True, null=False )
    # email = models.EmailField(max_length=150, blank=True, null=False )
    # phone = models.CharField(max_length=150, blank=True, null=False )
    # address = models.TextField()
    # city = models.CharField(max_length=150, blank=True, null=False )
    # state = models.CharField(max_length=150, blank=True, null=True)
    # country = models.CharField(max_length=150, blank=True, null=False )
    # pincode = models.CharField(max_length=150, blank=True, null=False )
    total_price = models.FloatField(blank=True, null=False )
    # payment_mode = models.CharField(max_length=150, blank=True, null=False )
    payment_id = models.CharField( max_length=150, blank=True, null=False , default=uuid.uuid4)
    stats = models.CharField( max_length=150, choices=order_status, default='pending')
    message = models.TextField(blank=True,null=True)
    tracking_no = models.CharField(max_length=150, blank=True, null=False )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order for {self.id} , has for  {self.user}   with {self.tracking_no}"
    
    class Meta:
        ordering = ('-create_at', )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=False )
    quantity = models.IntegerField(blank=True, null=False , default=1)

    def __str__(self):
        return f"order for {self.order.id} , for  user {self.order.user}   with {self.order.tracking_no}"
    
    
    
    