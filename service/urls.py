from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from TODO.views import TODOModelViewSet, ProjectModelViewSet
from users.views import CustomUserViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('TODOs', TODOModelViewSet, basename='TODOs')
router.register('projects', ProjectModelViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
