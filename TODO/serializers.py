from rest_framework.serializers import HyperlinkedModelSerializer

from users.serializers import UserTODOModelSerializer, UsersProjectModelSerializer
from .models import TODO, Project


class ProjectModelSerializer(HyperlinkedModelSerializer):
    creators_project = UsersProjectModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'repository', 'creators_project',)

    """
    The serializer is designed for output all fields on display of Project
    """


class TODOModelSerializer(HyperlinkedModelSerializer):
    project = ProjectModelSerializer()
    creator_keep = UserTODOModelSerializer()

    class Meta:
        model = TODO
        fields = ('creator_keep', 'body', 'project', 'created', 'modified', 'is_active',)

    """
    The serializer is designed for output all fields on display of TODO
    """
