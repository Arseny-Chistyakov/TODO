from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import TODOFilter
from .models import TODO, Project
from .serializers import ProjectGETModelSerializer, ProjectPOSTModelSerializer, TODOGETModelSerializer, \
    TODOPOSTModelSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectGETModelSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        queryset = Project.objects.all().order_by('name')
        name = self.request.query_params.get('name', '')
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset

    """
    The ViewSet is supported to filter the Project model by the name_field via param
    In this variant, filtering is done exclusively manually via param, without using the <django_filters> button
    """

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return ProjectPOSTModelSerializer
        return ProjectGETModelSerializer


class TODOPagination(PageNumberPagination):
    page_size = 10


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all().order_by('-modified')
    serializer_class = TODOGETModelSerializer
    pagination_class = TODOPagination
    filterset_class = TODOFilter

    """
    The ViewSet is supported to filter the TODO model by the project__name_field via param
    In this variant, automatic param generation by using filters.py with <django_filter> button or manually via param
    """

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return TODOPOSTModelSerializer
        return TODOGETModelSerializer
