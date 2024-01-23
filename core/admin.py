from django.contrib import admin
# from .models  import *

# Register your models here.
from .models  import Collections , Category , Item , Subcategory , MyFav , SocialMedia , Contact_Us, Colors
admin.site.register(Collections)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Subcategory)
admin.site.register(MyFav)
admin.site.register(SocialMedia)
admin.site.register(Contact_Us)
admin.site.register(Colors)

# @admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Exclude the 'created_at' field from the admin form
    exclude = ('created_at',)

