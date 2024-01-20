from django.contrib.sitemaps import Sitemap
from core.models import *   # Import your relevant models
from users.models import * 
from bloger.models import * 

class ItemSitemap(Sitemap):
    changefreq = 'daily'  # Set how frequently the page changes
    priority = 0.9  # Set the priority of this page
    def lastmod(self, obj):
        return obj.updated_at 
    
    def items(self):
        return Item.objects.all()
    
class CollectionSitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.8

    def lastmod(self, obj):
        return obj.updated_at
    
    def items(self):
        return Collections.objects.all()
    
class CategoresSitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    def items(self):
        return Category.objects.all()
    
class SubcategorySitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    def items(self):
        return Subcategory.objects.all()
    
# for users app 
class CustomUserSitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    def items(self):
        return CustomUser.objects.all()

# for blog App 
class CategorySitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    def items(self):
        return Category.objects.all()
    
class ArticleSitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    
    def lastmod(self, obj):
        return obj.date_updated 
    
    def items(self):
        return Article.objects.all()
    
class ProfileSitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    def items(self):
        return Profile.objects.all()
    
    
class CommentSitemap(Sitemap):
    changefreq = 'Daily'
    priority = 0.7
    
    def lastmod(self, obj):
        return obj.date_updated 
    
    def items(self):
        return Comment.objects.all()
    
sitemaps = {
    'items': ItemSitemap,
    'collections': CollectionSitemap,
    'categories': CategoresSitemap,
    'subcategory': SubcategorySitemap,
    'sustomUser': CustomUserSitemap,
    'category': CategorySitemap,
    'article': ArticleSitemap,
    'profile': ProfileSitemap,
    'comment': CommentSitemap,
}