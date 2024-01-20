from django.core.paginator import Paginator
from django.contrib import messages 
from django.http import JsonResponse 
from .models import Collections, Category, Item , Contact_Us
from carts.models import Cart 
from users.models import CustomUser
from sliders.models import SliderHome
from .forms import ItemForm 
from rating.models import RatingSystem
from django.shortcuts import render , redirect , get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# this fo pagination number of item per page 
items_per_page = 10  # You can adjust this as needed 
    
def index(request):
    categories = Collections.objects.all()    
    ads_item = Item.objects.filter(trending=True)[0:8]
    trend_item = Item.objects.filter(trending=True)[0:8]
    random_items = Item.objects.order_by('?')[0:8]
    recent_items = Item.objects.order_by('-created_at')[:8]
    editors_choice = Item.objects.filter(editors_choice=True)[:8]
    premium_items = Item.objects.filter(selling_price__gt=0)[:8]
    slider = SliderHome.objects.order_by('-created_at')[:4]
    
    return render(request , 'index.html', {
        "trend_item":trend_item,
        "premium_items":premium_items,
        "random_items":random_items,
        "recent_items":recent_items,
        "ads_item":ads_item,
        "editors_choice":editors_choice ,         
        "slider":slider,
        "categories":categories,
    })

def pages(request ):
    # trend_item = Item.objects.filter(trending=True)
    # paginator = Paginator(trend_item, items_per_page)
    # page_number = request.GET.get('page')
    # items_list = paginator.get_page(page_number)
    return render(request , 'core/pages/pages.html', {
        # "items_list":items_list,
    })

def trend_item(request ):
    trend_item = Item.objects.filter(trending=True)
    paginator = Paginator(trend_item, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    return render(request , 'core/pages/rending-item.html', {
        "items_list":items_list,
    })

def premium_items(request ):
    premium_items = Item.objects.filter(selling_price__gt=0 ) 
    paginator = Paginator(premium_items, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    return render(request , 'core/pages/rending-item.html', {
        "items_list":items_list,
    })

def recent_items(request ):
    recent_items = Item.objects.order_by('-created_at')
    paginator = Paginator(recent_items, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    return render(request , 'core/pages/recent-item.html', {
        "items_list":items_list,
    })

def random_items(request ):
    random_items = Item.objects.order_by('?')
    paginator = Paginator(random_items, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    return render(request , 'core/pages/random-items.html', {
        "items_list":items_list,
    })

def editors_choice(request ):
    editors_choice_item = Item.objects.filter(editors_choice=True)
    paginator = Paginator(editors_choice_item, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    return render(request , 'core/pages/editors-choice.html', {
        "items_list":items_list,
    })

def privacy(request  ):
    return render(request , 'core/privacy.html')

def terms(request  ):
    return render(request , 'core/terms.html')

def contact_us(request ):
    if request.method == "POST":
        # item_id = request.POST.get('item_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        submit = request.POST.get('submit')
        new_contactor = Contact_Us.objects.create(name=name, email=email, number=number, subject=subject )
        # new_contactor.is_valid():
        new_contactor.save()
        messages.info(request, 'Your Submit Successfuly look for email we well send message or in your phone  ')
    return render(request , 'core/contact_us.html', {
    })
    
def about_us(request ):
    return render(request , 'core/about_us.html', {})

def collections(request):
    categories = Collections.objects.all()
    return render(request , 'core/collections.html', { "categories":categories,  })

def collections_in_nav(request):
    categories = Collections.objects.all()
    print(categories)
    return render(request , 'base.html', { "categories":categories,  })

def category(request , collection , collection_id ):
    collection_item = Collections.objects.get(id=collection_id)
    categories = Category.objects.filter(collections=collection_item)
    category = Category.objects.filter(collections=collection_item).first()

    return render(request, 'core/categories.html', {
        "collection_item": collection_item,
        "collection": collection,
        "categories": categories,
        "category": category,
    })

    # def subcategory(request, collection, category, subcategory  ):
    #     category = get_object_or_404(Category, id=category_id)
    #     subcategories = Subcategory.objects.filter(category=category)
    #     subcategory = Subcategory.objects.filter()
    #     templates = Item.objects.filter(subcategory=subcategory)[:20]
        
    #     collection = Collections.objects.filter(category=category).first()
    #     categories = Category.objects.get(name=category)
        
    #     return render(request, 'core/subcategories.html', {
    #         "category": category,
    #         "subcategories": subcategories,
    #         "templates": templates,
    #         "collection": collection,
    #         "categories": categories,
    #     })

def category_details(request , collection ,category, category_id ):
    templates = Item.objects.filter(category=category_id)
    paginator = Paginator(templates, items_per_page)
    page_number = request.GET.get('page')
    items_list = paginator.get_page(page_number)
    
    trending = Item.objects.filter(category=category_id, trending=True)
    collection = Collections.objects.get(slug=collection)
    category = Category.objects.get(slug=category)
    return render(request, 'core/category_details.html', {
        "items_list": items_list,
        "trending   ": trending,
        'collection':collection,
        'category':category,
    })

    # editors_choice_item = Item.objects.filter(editors_choice=True)
    # paginator = Paginator(editors_choice_item, items_per_page)
    # page_number = request.GET.get('page')
    # items_list = paginator.get_page(page_number)
    # return render(request , 'core/pages/editors-choice.html', {
    #     "items_list":items_list,
    # })
    
def single_template(request, collection, category, template_id):
    template = Item.objects.get(id=template_id)
    collection = Collections.objects.get(slug=collection)
    category = Category.objects.filter(slug=category)
    template.number_of_views += 1
    
    template.save()
    if request.user.is_authenticated:
        if (RatingSystem.objects.filter(user=request.user,item=template)):
            rating_item = RatingSystem.objects.filter(user=request.user, item=template).first()
        else:
            rating_item = RatingSystem.objects.filter()
    else:
        rating_item = RatingSystem.objects.filter(item=template)
    
    rating = RatingSystem.objects.filter(item=template.id).count()
    # rating = RatingSystem.objects(item=template.id)
    
    
    return render(request, 'core/single_item.html', {
        "template": template,
        "collection": collection,
        "category": category,
        "rating_item": rating_item,
        "rating": rating,
    })

def get_carts_item(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, 'in/nav.html', {"carts":carts,})

def incres_number_of_download(request , pk):
    # item_id = request.POST['item_download_id']
    get_item = Item.objects.get(pk=pk)
    get_item.number_of_downloads  += 1
    get_item.number_of_views += 1
    get_item.save()
    return JsonResponse({"status":"download successfully ! "})

# @login_required
def add_item(request):
    if request.method == 'POST':
        form  = ItemForm(request.POST , request.FILES )
        if form.is_valid():
            title = request.POST.get('title')
            item = form.save(commit=False)
            item.slug = slugify(title)
            get_user = request.user
            user = CustomUser.objects.get(user=get_user)
            item.user = user
            item.save()
            messages.info(request, 'Your item Added sucessfuly waiting publish... ')
            return redirect('my_store')
    else:
        form = ItemForm()
        # messages.info(request, 'There Are wrang in your data ...! ')
    return render(request, 'core/add_item.html', {
        'form': form,
        'title': 'Add item',
        'button': 'Add item',
    })

# @login_required
# def edit_item(request, pk):
#     item_detial = items.objects.get(pk=pk)
#     # item_detial = get_object_or_404(items, pk)
#     if request.method == 'POST':
#         item =  items.objects.get(pk=pk)
#         # item = get_object_or_404(items, pk)
#         if (request.user == item.user) or request.user.is_staff:
#             form = itemForm(request.POST, request.FILES, instance=item )
#             if form.is_valid():
#                 form.save()
#                 messages.info(request, 'Your Changes has been added sucssessfuly... ')
#                 if request.META.get('HTTP_REFERER'):
#                 # print(f'request.resolver_match.url_name {request.resolver_match.url_name}')  # edit_item
#                 # print(f'request.META.get("HTTP_REFERER") {request.META.get("HTTP_REFERER")}') #  http://127.0.0.1:8000/my_library/edit_item/3/
#                     return redirect(request.META.get("HTTP_REFERER"))
#                 else:
#                     return redirect('my_store')
#         else:        
#             messages.info(request, "You hav'nt access to Edit This item but you edit send to auther as seagest ! ")
#             return redirect('my_store')
#     else:
#         # item = get_object_or_404(items, pk)
#         item = items.objects.get(pk=pk)
#         form = itemForm(instance=item)
#         return render(request, 'items/edit_item.html', { 
#                 'title':'edit item', 
#                 'form':form,  
#                 'item': item,
#                 'item_detial':item_detial
#                 })

#  # Login 

# @login_required
# def delet_item(request, pk):
#     profile = Profile.objects.get(items=pk)
    

#     if (request.user.is_staff):
#         item = items.objects.get(pk=pk)
#         item.available = 'draft'
#         item.save()
#         return JsonResponse({"status":f'The item - { item.name } -  Was Moved to Trash sucssessfuly '})
#         # messages.info(request,  f'The item - { item.name } -  Was Moved to Trash sucssessfuly ' )
#     elif (str(profile) == str(request.user)):
#         item = items.objects.get(pk=pk)
#         item.available = 'draft'
#         item.save()
#         # messages.info(request,  f'The item - { item.name } - Was Moved to Trash sucssessfuly' )
#         return JsonResponse({"status":f'The item - { item.name } -  Was Moved to Trash sucssessfuly '})
#     else:
#         return JsonResponse({"status": 'You not have access to delete this item '})
        
#         # messages.info(request,  'You not have access to delete this item ')
#     if request.META.get('HTTP_REFERER'):
#         return redirect(request.META.get("HTTP_REFERER"))
#     else:
#         return redirect('my_store')



