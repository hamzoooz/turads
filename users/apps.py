from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
# bookhope.com@gmail.com


    # Starts signals to create author profile.
    def ready(self):
        from users import signals