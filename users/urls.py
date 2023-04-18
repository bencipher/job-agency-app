from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'recruiters', views.RecruiterViewSet)
router.register(r'applicants', views.ApplicantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
