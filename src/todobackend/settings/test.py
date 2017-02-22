from base import *
import os

# Database
# https://docs.djangoproject.com/en/1.10/settings
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DATABASE','todobackend'),
            'USER': os.environ.get('MYSQL_USER','todo'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD','password'),
            'HOST': os.environ.get('MYSQL_HOST','localhost'),
            'PORT': os.environ.get('MYSQL_PORT','3386'),
        }
}