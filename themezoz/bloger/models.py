# Core Django imports.
# from django.contrib.auth.models import 
# from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from users.models import CustomUser

# Third party app imports
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Blog application imports.
from utils.blog_utils import count_words, read_time

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    image = models.ImageField(default='category-default.jpg', upload_to='category_images')
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        app_label = 'bloger'  # Ensure this matches the app name where Category is defined
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category_articles', kwargs={'slug': self.slug})

class Article(models.Model):

    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    # BLOG MODEL FIELDS
    category = models.ForeignKey(Category, on_delete=models.CASCADE,   related_name='articles')
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField()
    author = models.ForeignKey( CustomUser , on_delete=models.CASCADE,   related_name='articles')
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,   related_name='articles')
    image = models.ImageField(default='article-default.jpg', upload_to='article_pics')
    image_credit = models.CharField(max_length=250, null=True, blank=True)
    body = RichTextUploadingField(blank=True)
    tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True,   default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    count_words = models.CharField(max_length=50, default=0)
    read_time = models.CharField(max_length=50, default=0)
    deleted = models.BooleanField(default=False)


    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)
        app_label = 'bloger'  # Ensure this matches the app name where Category is defined
        

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})

class Profile(models.Model):
    user = models.OneToOneField( CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='profile-pic-default.jpg', upload_to='profile_pics')
    banner_image = models.ImageField(default='slider-1.jpg', upload_to='banner')
    job_title = models.CharField(max_length=100)
    bio = models.CharField(max_length=100,  help_text="Short Bio (eg. I love cats and games)")
    address = models.CharField(max_length=100,   help_text="Enter Your Address"  )
    city = models.CharField(  max_length=100, help_text="Enter Your City"  )
    country = models.CharField(max_length=100, help_text="Enter Your Country" )
    zip_code = models.CharField(max_length=100,  help_text="Enter Your Zip Code"   )
    twitter_url = models.CharField(max_length=250, default="#",   blank=True, null=True,  help_text= "Enter # if you don't have an account")
    instagram_url = models.CharField(max_length=250, default="#", blank=True, null=True,help_text="Enter # if you don't have an account")
    facebook_url = models.CharField(max_length=250, default="#", blank=True, null=True, help_text="Enter # if you don't have an account")
    github_url = models.CharField(max_length=250, default="#", blank=True, null=True, help_text= "Enter # if you don't have an account")
    email_confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        app_label = 'bloger'  # Ensure this matches the app name where Category is defined

class Comment(models.Model):

    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField()
    comment = models.TextField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,    related_name='comments')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date_created',)
        app_label = 'bloger'  # Ensure this matches the app name where Category is defined

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"
