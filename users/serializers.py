from rest_framework.serializers import HyperlinkedModelSerializer

from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'created', 'modified',)

    """
    The serializer is designed for output all fields on display of User
    """


class UserTODOModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

    """
    The serializer is designed for output custom fields on display for TODOs -> creator_keep
    """


class UserProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

    """
    The serializer is designed for output custom fields on display for TODOs -> project
    """


class UsersProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

    """
    The serializer is designed for output custom fields on display for Project -> creators_project
    """
