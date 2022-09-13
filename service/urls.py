from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from TODO.views import TODOModelViewSet, ProjectModelViewSet
from users.views import CustomUserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='TODO',
        default_version='0.1',
        description='Documentation to out project',
        contact=openapi.Contact(email='samson200289@mail.ru'),
        license=openapi.License(name='MIT License'), ),
    public=True,
    permission_classes=[permissions.IsAdminUser], )

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('TODOs', TODOModelViewSet, basename='TODOs')
router.register('projects', ProjectModelViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # TokenAuthentication
    path('api-token-auth/', views.obtain_auth_token),
    # JWTAuthentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Docs
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # GraphQL
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
