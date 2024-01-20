from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index' ),
    path('privacy' , views.privacy , name='privacy' ),
    path('terms' , views.terms , name='terms' ),
    path('contact_us' , views.contact_us , name='contact_us' ),
    # path('blog' , views.blog , name='blog' ),
    path('about-us' , views.about_us , name='about_us' ),

    path('collections' , views.collections , name='collections' ),
    path('collections_in_nav/' , views.collections_in_nav , name='collections_in_nav' ),
    path('collections/<str:collection>/<int:collection_id>' , views.category , name='category' ),
    path('collections/<str:collection>/<str:category>/<int:category_id>' , views.category_details , name='category_details' ),
    path('<str:collection>/<str:category>/<int:template_id>', views.single_template, name='single_template'),
    
    path('my_store/add/', views.add_item , name='add_item'),

    # path('my_store/edit_item/<int:pk>/', views.edit_item , name='edit_item'),
    # path('my_store/delet_item/<int:pk>', views.delet_item, name='delet_item'),
    path('incres_number_of_download/<int:pk>',views.incres_number_of_download, name='incres_number_of_download'),

    # pages 
    path('pages/',views.pages, name='pages'),
    path('pages/trending-item/',views.trend_item, name='trend_item'),
    path('pages/recent-item/',views.recent_items, name='recent_items'),
    path('pages/random-items/',views.random_items, name='random_items'),
    path('pages/editors-choice/',views.editors_choice, name='editors_choice'),
    path('pages/premium_items/',views.premium_items, name='premium_items'),
]