from rest_framework.serializers import HyperlinkedModelSerializer

from users.serializers import UserTODOModelSerializer, UsersProjectModelSerializer
from .models import TODO, Project


class ProjectModelSerializer(HyperlinkedModelSerializer):
    creators_project = UsersProjectModelSerializer(many=True, style={'base_template': 'input.html'})

    class Meta:
        model = Project
        fields = ('name', 'repository', 'creators_project',)

    """
    The serializer is designed for output all fields on display of Project
    """


class ProjectNameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name',)

    """
    The serializer is designed for output name_fields on display of Project
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


class TODOFilteringByProjectSerializer(HyperlinkedModelSerializer):
    project = ProjectNameSerializer()
    creator_keep = UserTODOModelSerializer(read_only=True)

    class Meta:
        model = TODO
        fields = ('creator_keep', 'body', 'project', 'is_active',)

    """
    The serializer is designed for output custom fields when filtering on display of TODO
    """
