from django.contrib.auth import get_user_model
User = get_user_model()

from django.db import models
from core.models import Item

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{ self.user } - { self.item }'


class LikeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{ self.user } - { self.item }'



