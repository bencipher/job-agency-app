from rest_framework import permissions, viewsets

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser]
