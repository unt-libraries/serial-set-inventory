from .base import *

SITE_ID = get_secret('SITE_ID')

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')

ADMINS = get_secret('ADMINS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DATABASES_NAME'),
        'USER': get_secret('DATABASES_USER'),
        'PASSWORD': get_secret('DATABASES_PASSWORD'),
        'HOST': get_secret('DATABASES_HOST'),
        'PORT': get_secret('DATABASES_PORT'),
    }
}

STATIC_URL = get_secret('STATIC_URL')

STATIC_ROOT = get_secret('STATIC_ROOT')
