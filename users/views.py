from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .models import Applicant, CustomUser, Organization, Recruiter
from .permissions import IsOrganizationOwner
from .serializers import (ApplicantSerializer, CustomUserSerializer,
                          CustomUserUpdateSerializer, OrganizationSerializer,
                          RecruiterSerializer, RecruiterUpdateSerializer)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return CustomUserUpdateSerializer
        return self.serializer_class


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsOrganizationOwner, IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = request.method == 'PATCH'
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        organization = serializer.save()

        return Response(RecruiterSerializer(organization).data)


class RecruiterViewSet(viewsets.ModelViewSet):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'list']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            pass
        elif self.request.method == 'PUT':
            return RecruiterUpdateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        user = request.user
        payload = request.data.copy()
        if user.is_authenticated:
            # return Response({}, 200)
            if hasattr(user, 'recruiter'):
                raise PermissionDenied(detail='A recruiter profile already exists for this account.')
            else:
                return Response({'error': 'user without recruiter profile denied'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = request.method == 'PATCH'
        serializer = self.get_serializer_class()
        serializer = serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
