# flake8: noqa
import os

from .base import *  # NOQA

DEBUG = True

# Database
# https://docs.djangop  roject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'copytypeidea_db',
        'USER': 'root',
        'PASSWORD': '@huqiao123',
        'HOST': '39.105.153.251',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8'}
    }
}