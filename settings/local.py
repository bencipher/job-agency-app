import os

from dotenv import load_dotenv

from .base import DATABASES

load_dotenv()
DEBUG = True
DATABASES['default']['ENGINE'] = os.getenv('POSTGRES_DB')
DATABASES['default']['NAME'] = os.getenv('POSTGRES_DB')
DATABASES['default']['USER'] = os.getenv('POSTGRES_USER')
DATABASES['default']['PASSWORD'] = os.getenv('POSTGRES_PASSWORD')
DATABASES['default']['HOST'] = os.getenv('POSTGRES_HOST', 'localhost')
DATABASES['default']['PORT'] = os.getenv('POSTGRES_PORT', '5432')
