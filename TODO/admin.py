from itertools import chain

from django.contrib import admin

from TODO.models import TODO, Project


@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ('body', 'creator', 'project', 'created', 'modified', 'is_active',)
    list_filter = ('creator', 'is_active',)
    fields = ('body', 'creator', 'project', 'created', 'modified', 'is_active',)
    readonly_fields = ('created', 'modified',)
    ordering = ('-created',)
    search_fields = ('creator__username', 'project__name', 'created', 'is_active')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def creator_names(self, obj):
        a = obj.users.values_list('username')
        return list(chain.from_iterable(a))

    list_display = ('name', 'repository', 'creator_names')
    readonly_fields = ('uid',)
    fields = ('name', 'repository', 'users',)
    search_fields = ('name', 'users__username',)
