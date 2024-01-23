from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField  # Assuming you're using CKEditor
from django.utils import timezone



class Collections(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    # created_by = models.ForeignKey(CustomUser ,  on_delete=models.CASCADE,   default=1)
    name = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    image_background = models.ImageField(upload_to="categories", null=True, blank=True, default='image_background.jpg')
    thumbnail_clooection = models.ImageField(upload_to="categories", null=True, blank=True, default='thumbnail_clooection.jpg')
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Trending')
    number_of_views = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self) :
        return f"{self.name}"

class Category(models.Model):
    collections = models.ManyToManyField(Collections, blank=True )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=150, blank=True, null=True )
    slug = models.SlugField(max_length=150, blank=True, null=True )
    image = models.ImageField(upload_to="categories", null=True, blank=True, default='default-pic-avatar.jpg')
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Trending')
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    number_of_views = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Auto-generate the slug if it's not provided
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

class Subcategory(models.Model):
    category = models.ManyToManyField(Category  )
    name = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to="categories", null=True, blank=True, default='default-pic-avatar.jpg')
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Trending')
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    number_of_views = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Auto-generate the slug if it's not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
       
       
class Colors(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
         
# Constants for choices fields
LANGUAGES = (
    ('en', 'English'),
    ('ar', 'Arabic'),
    ('oth', 'Others'),
    # Add other language options here
    )

AVAILABILITY_CHOICES = (
    ('publised', 'publised'),
    ('wiating', 'wiating'),
    ('draft', 'draft'),
    ('deleted', 'deleted'),
    )

COLORS = (
    ('red', 'red'),
    ('black', 'black'),
    ('gray', 'gray'),
    ('yellow', 'yellow'),
    # ('yellow', 'yellow'),
    )

class Item(models.Model):
    user = models.ForeignKey( CustomUser , on_delete=models.CASCADE, default=4)
    title = models.CharField(max_length=100)
    long_title = models.CharField(max_length=250, null=True, blank=True)
    file = models.FileField(upload_to="templates/files/", null=True, blank=True)
    weight  = models.FloatField (default=0)
    number_in_meter  = models.FloatField(default=0)
    thickness  = models.FloatField(default=0)
    colors = models.ManyToManyField(Colors ,  default='gray' )
    # available = models.CharField(max_length=10, )
    
    lenght  = models.FloatField(default=0)
    width  = models.FloatField(default=0)
    heigth  = models.FloatField(default=0)
    with_transport = models.BooleanField(default=False, help_text='0=defauwithout transport, 1=withtransport')
 
    url_download = models.URLField(null=True, blank=True)
    url_download2 = models.URLField(null=True, blank=True)
    url_downloa3 = models.URLField(null=True, blank=True)
    url_gitgub = models.URLField(null=True, blank=True)
    url_gitlab = models.URLField(null=True, blank=True)
    url_index = models.URLField(null=True, blank=True)
    url_readme = models.URLField(null=True, blank=True)
    url_one_drive = models.URLField(null=True, blank=True)
    url_google_drive = models.URLField(null=True, blank=True)
    url_gitbuck_drive = models.URLField(null=True, blank=True)
    demo = models.URLField(null=True, blank=True)
    demo1 = models.URLField(null=True, blank=True)
    demo2 = models.URLField(null=True, blank=True)
    demo3 = models.URLField(null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True )
    # subcategory = models.ManyToManyField(Subcategory , blank=True)
    slug = models.SlugField(unique=True, max_length=150 , null=True, blank=True )
    theme_image = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image1 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image2 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image3 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image4 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image5 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image6 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image7 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image8 = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    theme_image_url = models.URLField(null=True, blank=True)
    theme_image_url_1 = models.URLField(null=True, blank=True)
    theme_image_url_2 = models.URLField(null=True, blank=True)
    theme_image_url_3 = models.URLField(null=True, blank=True)
    theme_image_url_4 = models.URLField(null=True, blank=True)
    theme_image_url_5 = models.URLField(null=True, blank=True)
    theme_image_url_6 = models.URLField(null=True, blank=True)
    theme_image_url_7 = models.URLField(null=True, blank=True)
    theme_image_url_8 = models.URLField(null=True, blank=True)
    theme_image_url_9 = models.URLField(null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    language = models.CharField(max_length=3, choices=LANGUAGES, default='en')
    # version = models.IntegerField(blank=True, null=True , default=1.0 )
    available = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES, default='waiting')
    number_of_views = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    small_description = RichTextField(  blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    Features = RichTextField(blank=True, null=True)
    how_to_use = RichTextField(blank=True, null=True)
    number_of_paid = models.IntegerField(default=0)
    # number_pages = models.IntegerField(default=0)
    original_price = models.FloatField(default=0, null=True, blank=True)
    selling_price = models.FloatField(default=0, null=True, blank=True)
    size = models.BigIntegerField(blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Trending')
    editors_choice = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    tags = models.CharField(max_length=150, blank=True, null=True)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.title}"
    
    def save(self, *args, **kwargs):
        # Auto-generate the slug if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        # Set the updated_at field to the current time before saving
        
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        # Define the URL for a detail view of an item
        return reverse('item_detail', args=[str(self.title)])




class MyFav(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE )
    
    def __str__(self) -> str:
        return f'{self.user} - { self.item }'

class SocialMedia(models.Model):
    name = models.CharField(max_length=50 ) 
    url = models.URLField()
    icon  = models.ImageField(upload_to="templates/images/icon_social_media", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.url} "

class Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=800)
    create_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self) :
        return f'{self.name} - {self.subject} - {self.email} - {self.message} '
