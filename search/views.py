from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from core.models import Item

def search(request):
    query = request.GET.get('productsearch', '')
    
    items = Item.objects.filter(Q(title__icontains=query) | Q(meta_description__icontains=query) |
    Q(meta_title__icontains=query) |
    Q(meta_keywords__icontains=query) |
    Q(created_at__icontains=query) |
    Q(updated_at__icontains=query) |
    Q(how_to_use__icontains=query) |
    Q(Features__icontains=query) |
    Q(description__icontains=query) |
    Q(small_description__icontains=query) |
    Q(slug__icontains=query) |
    Q(published_date__icontains=query) |
    Q(tags__icontains=query), available='publised')

    return render(request, 'search/search.html', {
        'query': query,
        'items': items,
    })

def item_list(request):
    items = Item.objects.filter(available='publised').values_list('title' , flat=True)
    item_list = list(items)[0:100]
    # item_list = list(books)

    return JsonResponse(item_list, safe=False )

