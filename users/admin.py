from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('username', 'created', 'modified',)
    fields = ('username', 'first_name', 'last_name', 'email', 'created', 'modified',)
    readonly_fields = ('created', 'modified',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    ordering = ('-created',)
    # TODO: create beauty admin interface
