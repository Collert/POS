"""
Django settings for heucc_pos project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.urls import reverse_lazy
import socket

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SQUARE_ACCESS_TOKEN = os.getenv('SQUARE_ACCESS_TOKEN')
SQUARE_ENVIRONMENT = os.getenv('SQUARE_ENVIRONMENT')
SQUARE_DEVICE_ID = os.getenv('SQUARE_DEVICE_ID')
SQUARE_LOCATION_ID = os.getenv('SQUARE_LOCATION_ID')
SQUARE_WEBHOOK_SIGNATURE_KEY = os.getenv('SQUARE_WEBHOOK_SIGNATURE_KEY')
SQUARE_APPLICATION_ID = os.getenv('SQUARE_APPLICATION_ID')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
VAPID_PUBLIC_KEY = os.getenv('VAPID_PUBLIC_KEY')
VAPID_PRIVATE_KEY = os.getenv('VAPID_PRIVATE_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)mvvs#%dtv$1s)5ak4%!&g63-!&%tn8wtn0s21&ux*=!#9$b^$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('ENVIRONMENT') != "production"

MEDIA_ROOT = ''
MEDIA_URL = ''

LOGIN_URL = reverse_lazy('login_view')

ALLOWED_HOSTS = [
    "127.0.0.1", 
    "localhost", 
    "server.uahelp.ca", 
    "internal.uahelp.ca", 
    "local.internal.uahelp.ca",
    "f987-2605-8d80-483-d351-d9d2-4442-de38-1b9e.ngrok-free.app",
    "154.20.173.24"
    "154.20.173.24",
    "173.183.117.181"
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000", 
    "http://server.uahelp.ca", 
    "http://internal.uahelp.ca", 
    "http://local.internal.uahelp.ca",
    "https://f987-2605-8d80-483-d351-d9d2-4442-de38-1b9e.ngrok-free.app",
    "https://internal.uahelp.ca",
    "https://173.183.117.181"
    ]

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pos_server.apps.PosServerConfig',
    'webrtc',
    'landing',
    'misc_tools',
    'online_store',
    'inventory',
    'deliveries',
    'users',
    'mathfilters',
    'gift_cards',
    'payments',
    'events',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'heucc_pos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'online_store.context_processors.check_business_day',
            ],
        },
    },
]

WSGI_APPLICATION = 'heucc_pos.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.getenv('ENVIRONMENT') == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'heucc_restaurant',
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',  # Leave as an empty string to use the default port
        }
    }
    NOTIFICATIONS_HOST = "https://internal.uahelp.ca"
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    NOTIFICATIONS_HOST = "http://127.0.0.1:8000"

if 'local.internal.uahelp.ca' in socket.gethostname().lower():
    SECURE_PROXY_SSL_HEADER = None
else:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if os.getenv('ENVIRONMENT') == "production":
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
            'simple': {
                'format': '[{asctime}] "{message}"',
                'style': '{',
                'datefmt': '%d/%b/%Y %H:%M:%S',
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/home/collert/POS/debug.log',
                'formatter': 'simple',
            },
        },
        'loggers': {
            'django.server': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': False,
            },
            # Optionally, disable SQL query logging by setting django.db.backends to WARNING or ERROR
            'django.db.backends': {
                'handlers': ['file'],
                'level': 'WARNING',
                'propagate': False,
            },
        },
    }


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

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = '/home/collert/POS/heucc_pos/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'payments/static/'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
