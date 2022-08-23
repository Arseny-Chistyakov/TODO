from django_filters import rest_framework as filters

from TODO.models import TODO


class TODOFilter(filters.FilterSet):
    project__name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TODO
        fields = ['project__name']
