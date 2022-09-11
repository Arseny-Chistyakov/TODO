from rest_framework.serializers import ModelSerializer

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'username', 'first_name', 'last_name', 'email', 'created', 'modified', 'is_active',
                  'is_staff', 'is_superuser')

    """
    The serializer is designed for output all fields on display of User
    """


class UserPermissionSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'username', 'is_staff', 'is_superuser')
