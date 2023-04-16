import os

from dotenv import load_dotenv

from .base import *  # noqa

load_dotenv()
DEBUG = True

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
#
# DATABASES['default']['NAME'] = os.getenv('POSTGRES_DB')
# DATABASES['default']['USER'] = os.getenv('POSTGRES_USER')
# DATABASES['default']['PASSWORD'] = os.getenv('POSTGRES_PASSWORD')
# DATABASES['default']['HOST'] = os.getenv('POSTGRES_HOST', 'localhost')
# DATABASES['default']['PORT'] = os.getenv('POSTGRES_PORT', '5432')
