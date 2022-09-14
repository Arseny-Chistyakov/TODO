from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import User
from .models import TODO, Project


class ProjectGETModelSerializer(ModelSerializer):
    creators_project = serializers.SlugRelatedField(slug_field='username', queryset=User.objects, many=True)

    class Meta:
        model = Project
        fields = ('uid', 'name', 'repository', 'creators_project',)

    """
    The serializer is designed for output all fields on display of Project for GET(list) method
    """


class ProjectPOSTModelSerializer(ModelSerializer):
    creators_project = PrimaryKeyRelatedField(queryset=User.objects, many=True)

    class Meta:
        model = Project
        fields = ('uid', 'name', 'repository', 'creators_project',)

    """
    The serializer is designed for output all fields on display of Project for POST(create,delete, put, patch) method
    """


class TODOGETModelSerializer(ModelSerializer):
    creator_keep = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)
    project = serializers.SlugRelatedField(slug_field='name', queryset=Project.objects)

    class Meta:
        model = TODO
        fields = ('uid', 'creator_keep', 'body', 'project', 'created', 'modified', 'is_active',)

    """
    The serializer is designed for output all fields on display of TODO for GET(list) method
    """


class TODOPOSTModelSerializer(ModelSerializer):
    creator_keep = serializers.PrimaryKeyRelatedField(queryset=User.objects)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects)

    class Meta:
        model = TODO
        fields = ('uid', 'creator_keep', 'body', 'project', 'created', 'modified', 'is_active',)

    """
    The serializer is designed for output all fields on display of TODO for POST(create,delete, put, patch) method
    """
