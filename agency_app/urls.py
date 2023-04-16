from django.urls import include, path
from rest_framework import routers

from .views import JobDetailAPIView, JobListAPIView, JobViewSet

router = routers.DefaultRouter()
router.register(r'', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/', JobListAPIView.as_view(), name='job_list'),
    path('jobs/<uuid:pk>/', JobDetailAPIView.as_view(), name='job_detail'),
]
