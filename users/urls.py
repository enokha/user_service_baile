from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet  # Make sure 'users' is the correct app name.
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
