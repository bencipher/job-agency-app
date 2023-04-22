import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            try:
                User.objects.create_superuser(
                    username=os.getenv('SUPER_USERNAME'),
                    password=os.getenv('SUPER_USER_PASSWORD')
                )
            except Exception as e:
                print(f'Super user creation failed with error {str(e)}')
        print('Superuser has been created.')
