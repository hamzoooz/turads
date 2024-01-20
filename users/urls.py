from django.urls import path
from . import views
from .views import CustomRegistrationView
from allauth.socialaccount import views as socialaccount_views
from users.views import CustomLogoutView

urlpatterns = [
    path('@<str:username>' , views.user_detail , name='user_detail' ),
    path('my_store' , views.my_store , name='my_store' ),
    path('accounts/signup/', CustomRegistrationView.as_view(), name='custom_signup'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='custom_account_logout'),  # Custom logout URL
    # path('accounts/login/github/', socialaccount_views.github_login, name='github_login'),
    # path('accounts/login/facebook/', socialaccount_views.facebook_login, name='facebook_login'),
    # ...
]
