from django.db import models

# Create your models here.
class SliderHome(models.Model):
    title = models.CharField(max_length=20)
    description  = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True )
    image_url = models.URLField(null=True, blank=True )
    updated_at = models.DateTimeField(auto_now=True)
    number_of_views = models.IntegerField(default=0)
    number_of_clicks = models.IntegerField(default=0)
    url = models.URLField()

    def __str__(self) :
        return f"{self.title} - {self.description}"




