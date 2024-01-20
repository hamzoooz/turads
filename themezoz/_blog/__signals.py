from users.models import CustomUser 
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser 
from blog.models import Profile
# Blog application imports.
 
# Creates author profile immediately an account is created for her/him.
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# Saves author profile automatically after creating the profile.
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
 


 
    
    


