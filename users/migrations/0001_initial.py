# Generated by Django 3.2.12 on 2022-08-04 00:59

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='user', max_length=255, verbose_name='Логин')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменен')),
            ],
        ),
    ]
