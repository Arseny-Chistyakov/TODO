from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserModelSerializer


class UserPagination(PageNumberPagination):
    page_size = 20


class CustomUserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all().order_by('uid')
    pagination_class = UserPagination
    serializer_class = UserModelSerializer

    """
    The ViewSet is supported methods: List,Retrieve,Update
    """
