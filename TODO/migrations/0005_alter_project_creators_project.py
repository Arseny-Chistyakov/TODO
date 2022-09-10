# Generated by Django 3.2.12 on 2022-09-09 22:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TODO', '0004_alter_project_creators_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creators_project',
            field=models.ManyToManyField(related_name='creators_project', to=settings.AUTH_USER_MODEL,
                                         verbose_name='Пользователи, работающие над проектом'),
        ),
    ]
