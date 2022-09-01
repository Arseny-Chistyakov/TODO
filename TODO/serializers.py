from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import TODO, Project


class ProjectModelSerializer(ModelSerializer):
    creators_project = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)

    # creators_project = serializers.HyperlinkedRelatedField(view_name='users-detail', many=True,
    #                                                        queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ('uid', 'name', 'repository', 'creators_project',)

    """
    The serializer is designed for output all fields on display of Project
    """


class TODOModelSerializer(ModelSerializer):
    creator_keep = serializers.SlugRelatedField(slug_field='username', read_only=True)
    project = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = TODO
        fields = ('uid', 'creator_keep', 'body', 'project', 'created', 'modified', 'is_active',)

    """
    The serializer is designed for output all fields on display of TODO
    """
