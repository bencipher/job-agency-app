from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from agency_app.filters import JobFilter

from .models import Job
from .serializers import JobSerializer


class JobListAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = JobFilter
    ordering_fields = ('rate', 'date_posted')
    search_fields = ('location', 'title')
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Job.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.request.query_params.get('page')
        if page:
            page_queryset = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        serializer = JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def delete(self, request, *args, **kwargs):
        job = self.get_object()
        job.is_cancelled = True
        job.save()
        serializer = self.get_serializer(job)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        job = self.get_object()
        serializer = JobSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()
        job_serializer = JobSerializer(job)
        return Response(job_serializer.data)

    def patch(self, request, *args, **kwargs):
        job = self.get_object()
        serializer = JobSerializer(job, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()
        job_serializer = JobSerializer(job)
        return Response(job_serializer.data)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = JobFilter
    ordering_fields = ('rate', 'date_posted')
    search_fields = ('location', 'title')

    def destroy(self, request, *args, **kwargs):
        job = self.get_object()
        job.is_cancelled = True
        job.save()
        serializer = self.get_serializer(job)
        return Response(serializer.data)
