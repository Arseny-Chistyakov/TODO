import os

from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User

username_admin = os.getenv('USERNAME_ADMIN')
password_admin = os.getenv('PASSWORD_ADMIN')


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_superuser(username=username_admin, email='admin@mail.ru', is_staff=True, is_active=True,
                                      is_superuser=True, password=password_admin)
        User.objects.create(username='Test_user_11', first_name='Frew', last_name='Werf', email='user_11@vk.ru',
                            is_staff=False, is_active=True, is_superuser=False, password=make_password('sdvd13_232'))
        User.objects.create(username='Test_user_21', first_name='Grew', last_name='Werg', email='user_21@vk.ru',
                            is_staff=False, is_active=True, is_superuser=False, password=make_password('sdvd23_232'))
        User.objects.create(username='Test_user_31', first_name='Drew', last_name='Werd', email='user_31@vk.ru',
                            is_staff=False, is_active=True, is_superuser=False, password=make_password('sdvd33_232'))
