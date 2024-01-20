from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission ,AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.utils import timezone
# from django.contrib.auth import get_user_model
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
 
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)
# CustomUser 

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", null=True, unique=True, max_length=100)
    username = models.CharField(_('User Name'), max_length=150, unique=True)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to="users/images", default='cover-book-quran.jpg', null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    profile_cover_image = models.ImageField(upload_to="users/covers", default='cover-book-quran.jpg', null=True, blank=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    ordered = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_templates = models.IntegerField(default=0, blank=True, null=True)
    number_of_downloads = models.IntegerField(default=0, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    contact_facebook = models.URLField(blank=True, null=True)
    contact_twitter = models.URLField(blank=True, null=True)
    number_of_gifts = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    pro = models.BooleanField(default=False)

    # Add related_name to groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='profiles' , blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='profiles', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.id} - {self.username } - {self.email }"



@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    # You can add any additional profile-related logic here, if needed.
    pass

# class CustomUser(AbstractUser):
#     # Your CustomUser fields here
#     pass

# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     # Other fields for the profile
    
    
    