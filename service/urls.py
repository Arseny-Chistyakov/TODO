from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from TODO.views import TODOModelViewSet, ProjectModelViewSet
from users.views import CustomUserViewSet

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
]
