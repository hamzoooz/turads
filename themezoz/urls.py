from django.contrib.sitemaps.views import sitemap 
# from sitemaps import ItemSitemap  
from django.conf.urls.static import static
from django.conf import settings
from sitemaps import sitemaps

from django.contrib import admin
from django.urls import path , include 
# for render.com to deplay 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# sitemaps = {
#     'yourmodel': ItemSitemap,  # Map sitemap class to a name
# }

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('admin/', admin.site.urls),
    path('' , include('core.urls')),
    path('' , include('users.urls')),
    path('' , include('carts.urls')),
    path('' , include('wishlist.urls')),
    path('' , include('order.urls')),
    path('' , include('search.urls')),
    path('' , include('rating.urls')),
    path('' , include('sliders.urls')),
    path('' , include('payment.urls')),
    path("", include('dashbord.urls')),
    path("", include('admin_soft.urls')),
    # path('paypal/', include('paypal.standard.ipn.urls')),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('accounts/', include('allauth.urls')),
    # form blog 
    path('blog/', include('bloger.urls')),
#    path('api/v1/', include('blog.api.v1.routers.routers')), 
    
#     path('api-auth/', include('rest_framework.urls')),
#     path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

# handler404 = 'core.views.error_404_view'
