from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User
from .models import TODO, Project


class ProjectModelSerializer(ModelSerializer):
    creators_project = serializers.SlugRelatedField(slug_field='username', queryset=User.objects, many=True)


    class Meta:
        model = Project
        fields = ('uid', 'name', 'repository', 'creators_project',)

    """
    The serializer is designed for output all fields on display of Project
    """


class TODOModelSerializer(ModelSerializer):
    creator_keep = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)
    project = serializers.SlugRelatedField(slug_field='name', queryset=Project.objects)

    class Meta:
        model = TODO
        fields = ('uid', 'creator_keep', 'body', 'project', 'created', 'modified', 'is_active',)

    """
    The serializer is designed for output all fields on display of TODO
    """
