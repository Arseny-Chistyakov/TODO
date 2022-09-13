import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from TODO.models import Project, TODO
from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_TODOs = graphene.List(TODOType)
    projects_by_username = graphene.List(ProjectType, username=graphene.String())
    users_by_project = graphene.List(UserType, name=graphene.String())

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_TODOs(self, info):
        return TODO.objects.all()

    def resolve_projects_by_username(self, info, username=None):
        if username:
            return Project.objects.filter(creators_project__username=username)
        return Project.objects.all()

    def resolve_users_by_project(self, info, name=None):
        if name:
            return User.objects.filter(project__name=name)
        return User.objects.all()


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.create(**kwargs)
        return cls(user=user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        uid = graphene.UUID()
        username = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(uid=kwargs.get('uid'))
        user.username = kwargs.get('username')
        user.save()
        return cls(user=user)


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        uid = graphene.UUID()

    users = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
            User.objects.get(uid=kwargs.get('uid')).delete()
        except Exception as ex:
            return cls(users=User.objects.all())


class Mutations(ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()
    delete_user = UserDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
