# Django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import CustomUser
# from django.contrib.auth import get_user_model
from users.models import CustomUser 
from django.forms import TextInput, Select, FileInput , ModelForm, EmailInput, Textarea

# Third-party app imports
from ckeditor.widgets import CKEditorWidget

# bloger app imports
from bloger.models import Article
from bloger.models import Category
from bloger.models import Profile
from bloger.models import Comment


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
            "name": "username", "class": "input100",
            "placeholder": "Username"
        }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",  "class": "input100",
            "placeholder": "Password"
        }))
    
class UserRegisterForm(UserCreationForm):
    """
        Creates CustomUser registration form for signing up.
    """

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    email = forms.EmailField(max_length=254, required=True, widget=      forms.EmailInput(attrs={      "name": "email", "class": "input100",     "placeholder": "Email" }  ),   help_text='Required. Input a valid email address.' )
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={ "name": "password1", "class": "input100", "placeholder": "Password" } ), )
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={ "name": "password2", "class": "input100", "placeholder": "Confirm Password" } ), )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = { "username": forms.TextInput(attrs={ "name": "username", "class": "input100", "placeholder": "Username" }), }

class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:

        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Title",
                                     'id': "articleTitle"
                                     }),

            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }

class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                'name': "article-title",
                'class': "form-control",
                'placeholder': "Enter Article Title",
                'id': "articleTitle"
            }),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image",
            }

            ),

        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', ]
        widgets = {
            'name': TextInput(attrs={'aria-required': "true",
                                     'name': "contact-form-name",
                                     'class': "form-control",
                                     'placeholder': "Enter your name",
                                     'aria-invalid': "true"
                                     }),

            'email': EmailInput(attrs={'aria-required': "true",
                                       'name': "contact-form-email",
                                       'class': "form-control",
                                       'placeholder': "Enter your email",
                                       'aria-invalid': "true",
                                       }),

            'comment': Textarea(attrs={'name': "contact-form-message",
                                       'rows': "2",
                                       'class': "text-area-messge form-control",
                                       'placeholder': "Enter your comment",
                                       'aria - required': "true",
                                       'aria - invalid': "false"
                                       }),
        }

# dash board admin from 
class UserUpdateForm(forms.ModelForm):
    """
        Creates form for user to update their account.
    """
    email = forms.EmailField(widget=
                             forms.EmailInput(attrs={
                                                     'name': "email",
                                                     'id': "email",
                                                     'class': "form-control",
                                                    }
                                              ),
                             )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {

            'first_name': forms.TextInput(attrs={
                'name': "first-name",
                'class': "form-control",
                'id': "first-name"
            }),

            'last_name': forms.TextInput(attrs={
                'name': "last-name",
                'class': "form-control",
                'id': "last-name"
            }),

            'username': forms.TextInput(attrs={
                'name': "username",
                'class': "form-control",
                'id': "username"
            }),
        }

class ProfileUpdateForm(forms.ModelForm):
    """
       Creates form for user to update their Profile.
    """
    class Meta:
        model = Profile
        fields = [
                  'image', 'banner_image', 'job_title', 'bio', 'address',
                  'city', 'country', 'zip_code', 'twitter_url', 'github_url',
                  'facebook_url', 'instagram_url'
                  ]

        widgets = {

            'job_title': forms.TextInput(attrs={
                'name': "job-title",
                'class': "form-control",
                'id': "job-title"
            }),

            'bio': forms.Textarea(attrs={
                'name': "bio",
                'class': "form-control",
                'id': "bio", "rows": "5",
            }),

            'address': forms.TextInput(attrs={
                'name': "address",
                'class': "form-control",
                'id': "address"
            }),

            'city': forms.TextInput(attrs={
                'name': "city",
                'class': "form-control",
                'id': "city"
            }),

            'country': forms.TextInput(attrs={
                'name': "country",
                'class': "form-control",
                'id': "country"
            }),

            'zip_code': forms.TextInput(attrs={
                'name': "zip-code",
                'class': "form-control",
                'id': "zip-code"
            }),

            'image': forms.FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "profileImage",
            }),

            'banner_image': forms.FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "bannerImage",
            }),

            'facebook_url': forms.TextInput(attrs={
                'name': "facebook-account-url",
                'class': "form-control",
                'id': "github-account-url"
            }),

            'twitter_url': forms.TextInput(attrs={
                'name': "twitter-account-url",
                'class': "form-control",
                'id': "twitter-account-url"
            }),

            'instagram_url': forms.TextInput(attrs={
                'name': "instagram-account-url",
                'class': "form-control",
                'id': "instagram-account-url"
            }),

            'github_url': forms.TextInput(attrs={
                'name': "github-account-url",
                'class': "form-control",
                'id': "github-account-url"
            }),

        }


