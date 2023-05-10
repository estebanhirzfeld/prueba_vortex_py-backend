from .base import *
from decouple import config


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'prueba',
#         'USER': 'vortex',
#         'PASSWORD': 'vortex.23',
#         'HOST': 'localhost',
#         'PORT': '5433',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba_tecnica',
        'USER': 'postgres',
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'

