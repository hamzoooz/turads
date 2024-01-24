from pathlib import Path
import os, random, string , secrets 
from dotenv import load_dotenv
from decouple import config
import socket
# import logging
# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv() 

BASE_DIR = Path(__file__).resolve().parent.parent
 
# Generate a new secret key
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = ''.join(secrets.choice(chars) for i in range(50))

hostname = socket.gethostname()
print(hostname)

DEBUG = True  # Running on localhost

ALLOWED_HOSTS = ['*']  # For development (allow all hosts)
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # "admin_interface",
    # "colorfield",
    # 'grappelli',
    'admin_soft.apps.AdminSoftDashboardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    # Custom apps   # LOCAL
    'core',
    'users',
    'carts',
    'wishlist',
    "order",
    "search",
    "rating",
    "sliders",
    "dashbord",
    
    # gateway 
    "payment",
    # 'paypal.standard.ipn',
    
    # Therd part
    # 'rest_framework',
    # 'oauth2_provider',
    # 'social_django',
    # 'drf_social_oauth2',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
    # 'socialaccount',
    'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.twitter_oauth2',
    'ckeditor',
    'widget_tweaks',
    
#     # This for blog 
    'bloger',
   'django_filters',
#    'rest_framework',
   'taggit',
   'ckeditor_uploader',
   'crispy_forms',
#    'oauth2_provider',

   
   
   ]
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
    # 'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
        # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'themezoz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates') , os.path.join(BASE_DIR , "templates" , 'accounts')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
 
            ],

            'libraries': {
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'themezoz.wsgi.application'


# ENVIRONMENT = config('ENVIRONMENT', default='development')
# ENVIRONMENT = config('ENVIRONMENT', default='production ')

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# logging.getLogger('django.db.backends').setLevel(logging.ERROR)

# if ENVIRONMENT == 'development':  # For local development (SQLite)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# else:  # For production (PostgreSQL)

# alter user postgres with password 'Hamzoooz&0784512346#themezoz.com';     
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'themezoz',
#         'USER': 'themezoz',
#         'PASSWORD': 'Hamzoooz&0784512346#themezoz.com',
#         'HOST': 'localhost',  # Or your database host
#         'PORT': '5432',           # Port if not default
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'themezoz',
#         'USER': 'themezoz',  
#         'PASSWORD': 'Hamzoooz&0784512346#themezoz.com',
#         'HOST': 'localhost', # Or your database host
#         'PORT': '3306',      # Port if not default
#             'OPTIONS': {
#                 'init_command': 'SET sql_mode="STRICT_ALL_TABLES"',
#             },
#     }
# }
 
# ناس البيت وانت أمورك ماشة 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'themezoz',
#         'USER': 'themezoz',
#         'PASSWORD': 'Hamzoooz@0784512346#themezoz.com',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/static/'

 
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

ACCOUNT_EMAIL_REQUIRED = True
 
# for sandbox
# SQUARE_ACCESS_TOKEN = 'EAAAEDxQAypddU--TsBA93Cxi5jkuEui95yAXDuSldKpol8XjIdLQu31T60nNDgz'
# SQUARE_LOCATION_ID = 'LFGNJR0BERKDX'
# SQUARE_APPLICATION_ID = 'sandbox-sq0idb-Au4eolyhGqHHiAFCABtSpw'

# # for live or borductions 
# SQUARE_ACCESS_TOKEN = 'EAAAEVhoUBsqFzt1GunYCmuZJTaB5mLAnwc1KtLeNAXU9K98jIQHsRZpZzImOGwo'
# SQUARE_LOCATION_ID = 'LPZK4G04Z6TDW'
# SQUARE_APPLICATION_ID = 'sq0idp-2qbMEnkB88yC0Uk2UYOiyQ'

# SQUARE_LOCATION_ID = 'your_square_location_id'
# SQUARE_ACCESS_TOKEN = 'your_square_access_token'
# settings.py

# for live 
# id
# ARZ_CBKui5x0KurZlgovXcdSTQfbk_8FEEMQ5Q5eXlwkekSkmk1o3QHb-JROPSYD_rmvGvsP5BE-LClb
# secrt key 
# EFZykCjYwRAcIVwe3e9erjdrvdepH-R79zHurCtyDNfQ1CcrxKVUgIflr9CrEg3rvEnJkhf5HWYnzgsL

# # for hamzoooz.sd
# PAYPAL_CLIENT_ID = 'AfJGmyLywHRlfnRW_crFk-noqxHF-tC_OXpEfzEzlivKm5ulYuNlUcdutB6_u3CYca-KOiMPZeKmGUf2'
# PAYPAL_SECRET = 'EHOrO4iHlLr5ASxrJtToJn2qrXJ4EHK55AoNcy01lteGF_rzJ_jpYctDNKnnw2vEg5NJ3TKxPrq-TUau'

# for hamzoooz.sd sandbox 
# PAYPAL_MODE = 'sandbox'  # Use 'sandbox' or 'live'
# PAYPAL_CLIENT_ID = 'ARZmOUSD_wF9pK8jjZBMTForN-817t8eeYT-avlIb0-m6KLTnsQthsHxrz31FR9wggDm0c_NUAVACaZ3'
# PAYPAL_SECRET = 'EB1iU2yzl_uJPrefZoQViKWO7F_nJSytNuoC6sdZfI6a7J4zMN8yDNEtaT4dnzsP1b_dP3khV-DhKvLA'

# for themezoz.sd for live this ID = 47JXMTE749N3Q
PAYPAL_MODE = 'live'  # Use 'sandbox' or 'live'
PAYPAL_CLIENT_ID = 'ARB5VUCOPAx-qwU3WlLln0TdGVgKyPfGc--11OU2EEnW4XNE0it_Kj_oOmpIeCkmAeHsVJ0p-98gGb4X'
PAYPAL_CLIENT_SECRET = 'EAIBt2aMTcquqxHstKZUQlV3Th2MFIr3JWQpEcHUgGE2kFqAg7Uwp-gj1H1o62AxT5fLWdoLcOMFMpS7'


# # sandbox for bookhope.com
# PAYPAL_CLIENT_ID = 'AfwHQIMm7KtwRxs3UDDXblG_I9BH-hxYBuK9pN73NepWh81sG4S5UNqRfEjTageN-0TGbroWCqHfVIu5'
# PAYPAL_SECRET = 'EGctkWMhV4jsnzGMj-m7G4naHaJPvzYumi5gKkB6tfDpULy2ARSCGXjLOvUZ8hH-etyMw-3hvIwz1ifN'

# # live for bookhope.com
# PAYPAL_CLIENT_ID = 'AX2p9L08fPeLg8nebwmNpPLV3WPr9oET54OSUp0yhDcsk7R4xNHZMZnnjDYJOs-VNnRflXCXt1p8F2oo'
# PAYPAL_SECRET = 'EPBpMOnpz_si6pTtLh_OMHOMYx0i06-9gIlQ0SPygynBx7u58QaQYA9n3S-DEhsjs1C-ryvdow8VtMzN'
# PAYPAL_CLIENT_ID = 'AZXiQEhWJydPBpWyh7sO6KvgqbyqcMhPRyGzMsjaHTvaqXRIMvS14fKPT23wRQqrDe8jgETyAfhe4KQV'
# PAYPAL_SECRET = 'EAYMShjZl0UPZORfUa2-bDQDq85c3V-nSMGgAxusqOnwe8MG9VOvuU_5cPzsDEpAqo5ua6nRAkMqDL-g'

# PAYPAL_RECEIVER_EMAIL = 'your_paypal_email@example.com'
# # Set PayPal mode: live or sandbox
# PAYPAL_TEST = True  # Set to False for live transactions

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

CKEDITOR_UPLOAD_PATH = 'media/cheditor/'
CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default':
        {'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
                'youtube'
            ]),
        },
}


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]


SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': 'da9f134b4296d6ef7a0c',
            'secret': '7ef2ea70a9f8687ddec52a4bb969bf8497dbfd16',
            # 'client_id': 'da9f134b4296d6ef7a0c',
            # 'secret': '7a3f6fc3fe3808e384d4b2ff9ca6b3b37f471714',
            'key': '',
        },
        'SCOPE': ['user',  'email'],  # Customize the scope as needed
        'VERIFIED_EMAIL': True,   # Ensure verified email
        # 'SCOPE': ['user', 'repo' , 'email'],  # Customize the scope as needed
    },
    'google': {
        'APP': {
            # ssh -i "themezoz.com.pem" ubuntu@ec2-18-209-176-152.compute-1.amazonaws.com
            # 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
            'client_id': '194114353107-pvruo5hlgau5pd4s5q6hk0t5kc30rg4k.apps.googleusercontent.com',
            'secret': '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',
            'key': '',
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    # scrit =  bcb0708b9db37f0650a6ad8eef469f42
    #id =  1716742632145556
    'facebook': {
        'APP': {
            'client_id': '1716742632145556',
            'secret': 'bcb0708b9db37f0650a6ad8eef469f42',
            # 'client_id': '995743558317906',
            # 'secret': 'ed34ac8b2b03d7260204ee209d7f290d',
        },
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
    },
    # 'facebook': {
    #     'METHOD': 'oauth2',
    #     'SCOPE': ['email', 'public_profile'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'email',
    #         'name',
    #         'first_name',
    #         'last_name',
    #         'verified',
    #         'locale',
    #         'timezone',
    #         'link',
    #         'gender',
    #         'updated_time',
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'LOCALE_FUNC': 'path.to.callable',
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v10.0',
    # },Hamzoooz@0784512346#themezoz.com
    #  APP ID  =  27907813 
    # API Key =  pfjk27Xqr9YtQa6DV24bAmrg6
    # API Key Secret  =  tc3NMVj9QqqkFwVDPokMvSuVH07ZfpP8Z1xPerHV35NtlClFlV
    # Client ID  =  VHNXZ0FZX1Vra284SDl1SEZvM1I6MTpjaQ
    # client Secret  =  j0zVLzCo5oQ6Y7N1L0BRkpsNob_V7BOrWk1Ou-NyX34UC2s2cH
    'twitter': {
        'APP': {
            # clent id eVpnLUlaR21iVnpfdllqVG5TSFU6MTpjaQ
            # cleant secrit key  V2E8z_vTvAm7mlSvTRxb0DMks9rSFPuv5Ck-2zl2Q6jtIYD2Gd
            # API Key   =  GvLGBIIAY0POAI1qnwcerOWAb
            # API Key Secret =   1O1fe8By19XW93VEvnUG5FPWMHcpSniv7pL5iWXs7JJ6jQXe29
            'client_id': 'eVpnLUlaR21iVnpfdllqVG5TSFU6MTpjaQ',
            'secret': 'V2E8z_vTvAm7mlSvTRxb0DMks9rSFPuv5Ck-2zl2Q6jtIYD2Gd',
        }
    },
    'apple': {
        'APP': {
            'client_id': 'YOUR_APPLE_CLIENT_ID',
            'secret': 'YOUR_APPLE_CLIENT_SECRET',
            'KEY_ID': '<YOUR_KEY_ID>',
            'KEY_FILE': '<YOUR_KEY_FILE_PATH>',
            'SCOPE': [
                'email',
            ]
        }
    },
# Application (client) ID : 21d5d126-e227-4949-bd7d-0f2fa5bf4041
# Object ID : 14999494-caa9-4f12-ae8d-cc150fe6a720
# Directory (tenant) ID :0714ee65-2b1d-426c-9197-b7104c80cfcd

    'microsoft': {
        'CLIENT_ID': '<YOUR_CLIENT_ID>',
        'CLIENT_SECRET': '<YOUR_CLIENT_SECRET>',
        'RESOURCE': 'https://graph.microsoft.com',
        'SCOPE': [
            'openid',
            'profile',
            'email',
        ]
        },
    'vk': {
        'APP': {
            'client_id': 'YOUR_VK_CLIENT_ID',
            'secret': 'YOUR_VK_CLIENT_SECRET',
        }
    },
}

LOGIN_REDIRECT_URL = '/'

# 194114353107-pvruo5hlgau5pd4s5q6hk0t5kc30rg4k.apps.googleusercontent.com

# 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

AUTH_USER_MODEL = 'users.CustomUser'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
# ACCOUNT_AUTHENTICATION_METHOD = ('username', 'email')

AUTHENTICATION_METHOD = "USERNAME_EMAIL"
