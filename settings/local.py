import os

from dotenv import load_dotenv

from .base import *  # noqa

load_dotenv()
# no dev dependency library in main code,
# local should not be committed or removed later on
DEBUG = True

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
print(DATABASES)
