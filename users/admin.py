from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email', 'created', 'modified',)  # кастомизация в карточке
    readonly_fields = ('created', 'modified',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)  # поиск по выбранному столбцу
    ordering = ('-created',)  # сортировка по умолчанию по выбранному столбцу
