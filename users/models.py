from uuid import uuid4

from django.db import models


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    username = models.CharField(max_length=255, default='user', verbose_name='Логин')
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, verbose_name='Создан')
    modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Изменен')

    def __str__(self):
        return f'{self.username}'
