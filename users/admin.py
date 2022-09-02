from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import UserChangeForm
from users.models import User


class UserAdmin(UserAdmin):
    form = UserChangeForm
    list_display = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('username', 'created', 'modified',)
    # fields = ('username', 'first_name', 'last_name', 'email', 'created', 'modified',)
    readonly_fields = ('created', 'modified',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    ordering = ('-created',)
    # TODO: create beauty admin interface


admin.site.register(User, UserAdmin)
