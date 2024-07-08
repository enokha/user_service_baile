from django.contrib.auth.models import User
from rest_framework import viewsets, permissions  # Import the permissions module
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]  # No authentication required to create user
        else:
            permission_classes = [permissions.IsAuthenticated]  # Default permission class
        return [permission() for permission in permission_classes]