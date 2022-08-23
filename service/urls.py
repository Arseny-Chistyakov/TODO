from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from TODO.views import TODOModelViewSet, ProjectModelViewSet
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('TODOs', TODOModelViewSet)
router.register('projects', ProjectModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
