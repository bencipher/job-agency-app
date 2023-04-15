from django.urls import path

from .views import JobDetailAPIView, JobListAPIView

urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job_detail'),
]
