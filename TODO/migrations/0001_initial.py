# Generated by Django 3.2.12 on 2022-08-18 20:19

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название проекта')),
                ('url', models.URLField(blank=True, max_length=256, null=True, verbose_name='Ссылка на репозиторий')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Пользователи, работающие над проектом')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Текст заметки')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создана')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменена')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TODO.project',
                                                 verbose_name='Проект, где создана заметка')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                              verbose_name='Пользователь, создавший заметку')),
            ],
        ),
    ]