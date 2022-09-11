# Generated by Django 3.2.12 on 2022-08-28 23:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TODO', '0002_auto_20220822_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creators_project',
            field=models.ManyToManyField(related_name='project', to=settings.AUTH_USER_MODEL,
                                         verbose_name='Пользователи, работающие над проектом'),
        ),
    ]