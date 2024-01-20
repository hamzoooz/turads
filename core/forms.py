from django import forms
# from ckeditor.fields import RichTextField
from .models import  Item
# from django.forms import BaseForm, BaseModelForm


   #  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Name of Book '}))
   #  file = forms.CharField(widget=forms.FileInput( attrs={'class': ' form-control my-2 class-file '}))
   #  sample = forms.CharField(widget=forms.FileInput( attrs={'class': ' form-control my-2 class-sample '}))
   #  category = forms.CharField(widget=forms.SelectMultiple( attrs={'class': ' form-control my-2 class-category '}))
   #  book_image = forms.CharField(widget=forms.FileInput( attrs={'class': ' form-control my-2 class-book_image '}))
   #  number_pages = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-number_pages ' }))
   #  language = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-language ' }))
   #  short_link = forms.URLField(widget=forms.URLInput(attrs={'class': ' form-control my-2 class-short_link '}))
   #  isnn = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-isnn ' }))
   #  edition = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-edition ' }))
   #  published_house = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-published_house ' }))
   #  number_of_views = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-number_of_views ' }))
   #  small_descrption = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-small_descrption ' }))
   #  descrption = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-descrption ' }))
   #  descrption = RichTextField()
   #  quantity = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-quantity ' }))
   #  original_price = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-original_price ' }))
   #  selling_price = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-selling_price ' }))
   #  type_of_book = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-type_of_book ' }))
   #  size = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-size ' }))
   #  tags = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-tags ' }))
   #  meta_tilte = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-meta_tilte ' }))
   #  meta_keyword = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-meta_keyword ' }))
   #  meta_description = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-meta_description ' }))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Set the model to Item
        fields = (
            # "title", "long_title", "file", "url_download", "url_download2", "url_downloa3",
            # "url_gitgub", "url_gitlab", "demo", "demo1", "demo2", "demo3",
            # "category", "subcategory", "slug", "theme_image", "theme_image1",
            # "theme_image2", "theme_image3", "theme_image4", "theme_image5",
            # "theme_image6", "theme_image7", "theme_image8", "theme_image9",
            # "thumbnail", "language", "version", "small_description",
            # "description", "Features", "how_to_use", "original_price",
            # "selling_price", "size", "tags", "meta_title", "meta_keywords",
            # "meta_description"
            "__all__"
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2 class-title'}),
            'long_title': forms.TextInput(attrs={'class': 'form-control my-2 class-long_title'}),
            'file': forms.FileInput(attrs={'class': 'form-control my-2 class-file'}),
            'url_download': forms.TextInput(attrs={'class': 'form-control my-2 class-url_download'}),
            'url_download2': forms.TextInput(attrs={'class': 'form-control my-2 class-url_download2'}),
            'url_downloa3': forms.TextInput(attrs={'class': 'form-control my-2 class-url_downloa3'}),
            'url_gitgub': forms.TextInput(attrs={'class': 'form-control my-2 class-url_gitgub'}),
            'url_gitlab': forms.TextInput(attrs={'class': 'form-control my-2 class-url_gitlab'}),
            'demo': forms.TextInput(attrs={'class': 'form-control my-2 class-demo'}),
            'demo1': forms.TextInput(attrs={'class': 'form-control my-2 class-demo1'}),
            'demo2': forms.TextInput(attrs={'class': 'form-control my-2 class-demo2'}),
            'demo3': forms.TextInput(attrs={'class': 'form-control my-2 class-demo3'}),
            'category': forms.Select(attrs={'class': 'form-control my-2 class-category'}),
            'subcategory': forms.Select(attrs={'class': 'form-control my-2 class-subcategory'}),
            'slug': forms.TextInput(attrs={'class': 'form-control my-2 class-slug'}),
            'theme_image': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image'}),
            'theme_image1': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image1'}),
            'theme_image2': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image2'}),
            'theme_image3': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image3'}),
            'theme_image4': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image4'}),
            'theme_image5': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image5'}),
            'theme_image6': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image6'}),
            'theme_image7': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image7'}),
            'theme_image8': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image8'}),
            'theme_image9': forms.FileInput(attrs={'class': 'form-control my-2 class-theme_image9'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control my-2 class-thumbnail'}),
            'language': forms.Select(attrs={'class': 'form-control my-2 class-language'}),
            'version': forms.TextInput(attrs={'class': 'form-control my-2 class-version'}),
            'small_description': forms.Textarea(attrs={'class': 'form-control my-2 class-small_description'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2 class-description'}),
            'Features': forms.Textarea(attrs={'class': 'form-control my-2 class-Features'}),
            'how_to_use': forms.Textarea(attrs={'class': 'form-control my-2 class-how_to_use'}),
            'original_price': forms.TextInput(attrs={'class': 'form-control my-2 class-original_price'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control my-2 class-selling_price'}),
            # 'size': forms.TextInput(attrs={'class': 'form-control my-2 class-size'}),
            'tags': forms.TextInput(attrs={'class': 'form-control my-2 class-tags'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control my-2 class-meta_title'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control my-2 class-meta_keywords'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control my-2 class-meta_description'}),
        }




class ContactUsForm(forms.ModelForm):
    pass 
