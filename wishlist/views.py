from django.shortcuts import render, redirect 
from django.http import JsonResponse
from wishlist.models import WishList , LikeItem
from core.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def wishlist(request):
    wishlists = WishList.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlists': wishlists})

def add_to_wishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            item_id = int(request.POST.get('item_id'))
            item_check = Item.objects.get(id=item_id)
            if (item_check):
                if (WishList.objects.filter(user=request.user , item=item_id)):
                    return JsonResponse({'status': "Item Already in Favoret List "})
                else:
                    WishList.objects.create(user=request.user, item=item_check)
                    return JsonResponse({'status': "Your Item added Successfuly to Favoret  "})
            else:
                return JsonResponse({'status': "No Such Item Found "})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')

def remove_from_wishlist(request):
    if request.method == "POST":
        item_id = int(request.POST.get('item_id'))
        wishlistitem = WishList.objects.filter(user=request.user, item=item_id)
        if (wishlistitem):
            wishlistitem.delete()
        return JsonResponse({'status':'The item Removed from Favoret successfully '})


def add_like(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            item_id = int(request.POST.get('item_id'))
            item_check = Item.objects.get(id=item_id)
            if (item_check):
                if (LikeItem.objects.filter(user=request.user , item=item_id)):
                    item = Item.objects.get(item=item_id)
                    item.number_of_likes -= 1
                    return JsonResponse({'status': "Fascinating  ^_^  "})
                else:
                    LikeItem.objects.create(user=request.user, item=item_check)
                    item = Item.objects.get(item=item_id)
                    item.number_of_likes += 1
            else:
                return JsonResponse({'status': "No Such Item Found "})
    return redirect('/')


def add_dis_like(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            item_id = int(request.POST.get('item_id'))
            item_check = Item.objects.get(id=item_id)
            if (item_check):
                if (LikeItem.objects.filter(user=request.user , item=item_id)):
                    item = Item.objects.get(item=item_id)
                    item.number_of_likes -= 1
                    return JsonResponse({'status': "We Are sory for this ^;^  "})
                else:
                    LikeItem.objects.create(user=request.user, item=item_check)
                    item = Item.objects.get(item=item_id)
                    item.number_of_likes += 1
            else:
                return JsonResponse({'status': "No Such Item Found "})
    return redirect('/')

