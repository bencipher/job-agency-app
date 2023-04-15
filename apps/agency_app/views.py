from rest_framework import generics
from rest_framework.response import Response

from .models import Job
from .serializers import (CreateJobSerializer, GetJobQueryParamsSerializer,
                          JobSerializer)


class JobListAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        contract_type = self.request.query_params.get('contractType', None)
        if contract_type is not None:
            queryset = queryset.filter(contract_type=contract_type)
        date_since_posted = self.request.query_params.get('dateSincePosted', None)
        if date_since_posted:
            queryset = queryset.filter(date_posted__gte=date_since_posted)
        sort_by = self.request.query_params.get('sortBy', 'datePosted')
        if sort_by == 'rate':
            queryset = queryset.order_by('rate')
        else:
            queryset = queryset.order_by('-date_posted')
        return queryset

    def list(self, request, *args, **kwargs):
        query_params_serializer = GetJobQueryParamsSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CreateJobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()
        job_serializer = JobSerializer(job)
        headers = self.get_success_headers(job_serializer.data)
        return Response(job_serializer.data, status=201, headers=headers)


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
