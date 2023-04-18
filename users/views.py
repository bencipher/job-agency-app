from rest_framework import viewsets

from .models import Applicant, CustomUser, Organization, Recruiter
from .serializers import (ApplicantSerializer, CustomUserSerializer,
                          OrganizationSerializer, RecruiterSerializer)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAdminUser]


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
