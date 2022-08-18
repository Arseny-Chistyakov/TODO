from django.contrib import admin

from TODO.models import TODO, Project


@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'project', 'created', 'modified', 'is_active',)
    list_filter = ('user', 'is_active',)
    fields = ('body', 'user', 'project', 'created', 'modified', 'is_active',)
    readonly_fields = ('created', 'modified',)
    ordering = ('-created',)
    # search_fields = ('user', 'project', 'created', 'is_active')
    # TODO: manytomany dont support search


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)
    list_filter = ('users',)
    fields = ('name', 'url', 'users',)
    ordering = ('-users',)
    # search_fields = ('users',)
    # TODO: manytomany dont support search
