from uuid import uuid4

from django.db import models

from users.models import User


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    name = models.CharField(max_length=256, verbose_name='Название проекта')
    url = models.URLField(max_length=256, blank=True, null=True, verbose_name='Ссылка на репозиторий')
    users = models.ManyToManyField(User, verbose_name='Пользователи, работающие над проектом')

    def __str__(self):
        return f'Project: {self.name} by {self.users}'


class TODO(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    body = models.TextField(max_length=1024, blank=True, null=True, verbose_name='Текст заметки')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь, создавший заметку')
    project = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name='Проект, к которому создана заметка')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, verbose_name='Создана')
    modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Изменена')
    is_active = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f'Create by <{self.user}>' \
               f'{self.body}.'
