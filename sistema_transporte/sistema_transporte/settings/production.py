from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba_tecnica',
        'USER': 'postgres',
        'PASSWORD': 'wilson2001',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'