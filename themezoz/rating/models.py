from django.db import models
from django.db.models import Count, Sum, Avg 
from core.models import Item 
from users.models import CustomUser

class RatingSystem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey( Item, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    rate_in = models.CharField(max_length=255, default='item_dateil', null=True, blank=True)
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True)
    def get_total_rating(self):
        return len(self.item.rating) # test Sum if does not work 
    

    def get_avg(self):
        avg_rating = Avg(self.rating) 
        return avg_rating 

    def __str__(self):
        # return f'{self.user.username} rate {self.book.name} by {self.rating} av = {  self.get_total_rating}'
        return f'{self.user.username} rate {self.item.title} by {self.rating}'
        # return f'{self.user.username} rate {self.book.name}  av = {  self.get_total_rating}'
    
# class RatingSystemUser(models.Model):
#     profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#     rate_in = models.CharField(max_length=255, default='user_dateil', null=True, blank=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now_add=True)

#     def get_avra_rate(self):
#         return Avg(self.rating) / 5

#     def get_total_rating(self):
#         return Count(self.rating)

#     def __str__(self):
#         return f'{self.user.username} rate {self.user.username} by {self.rating}'