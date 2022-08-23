from itertools import chain

from django.contrib import admin

from TODO.models import TODO, Project


@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ('body', 'creator_keep', 'project', 'created', 'modified', 'is_active',)
    list_filter = ('creator_keep', 'is_active',)
    fields = ('body', 'creator_keep', 'project', 'created', 'modified', 'is_active',)
    readonly_fields = ('created', 'modified',)
    ordering = ('-created',)
    search_fields = ('creator_keep__username', 'project__name', 'created', 'is_active')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def creator_names_of_project(self, obj):
        a = obj.creators_project.values_list('username')
        return list(chain.from_iterable(a))

    list_display = ('name', 'repository', 'creator_names_of_project')
    readonly_fields = ('uid',)
    fields = ('name', 'repository', 'creators_project',)
    search_fields = ('name', 'creators_project__username',)
