from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from users.models import CustomUser
from core.models import Item
from .models import *

def rating_item(request, id):
    if request.method == "POST":
        if request.user.is_authenticated:
            item = get_object_or_404(Item, id=id)
            print(item)
            rating = request.POST.get('value')
            print(rating)
            check_rating = RatingSystem.objects.filter( user=request.user, item=item).exists()
            if (check_rating):
                update_rating = RatingSystem.objects.get(user=request.user, item=item)
                update_rating = RatingSystem.objects.filter( user=request.user,  item=item).update(rating=rating)
            else:
                new_rating = RatingSystem.objects.create(user=request.user, item=item, rating=rating)
            return JsonResponse({'status': 'thank\'s for rating this Item  '})
        else:
            # return redirect('login')
            return JsonResponse({'status': 'login requer to rate this item (^_^)'})
    return redirect('/')

# ################################################################################
# def rating_user(request, user):
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             user = get_object_or_404(CustomUser, profile=user )
#             rating = request.POST.get('value')
#             check_rating = RatingSystemUser.objects.filter(user=request.user, profile=user ).exists()
#             if (check_rating):
#                 update_rating = RatingSystemUser.objects.get(user=request.user, profile=user )
#                 update_rating = RatingSystemUser.objects.filter( user=request.user,  profile=user ).update(rating=rating)
#             else:
#                 new_rating = RatingSystemUser.objects.create(user=request.user, profile=user , rating=rating)
#             return JsonResponse({'status': 'thank\'s for rating to help other users '})
#         else:
#             return JsonResponse({'status': 'login requer to rate this item'})
#     return redirect('/')
