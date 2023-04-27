from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient

from .models import Recruiter


class RecruiterViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.recruiter = mixer.blend('users.Recruiter')
        self.user = mixer.blend('users.CustomUser')
        self.valid_payload = {
            "user": {
                "email": "test23@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password": "password"
            },
            "organization": {
                "name": "Test Organization",
                "address": "123 Test Street"
            },
            "job_title": "Test Job Title",
            "phone_number": "555-1234"
        }
        self.invalid_payload = {
            "user": {
                "first_name": "Test",
                "last_name": "User",
                "password": "password"
            },
            "organization": {
                "address": "123 Test Street"
            },
            "job_title": "Test Job Title",
        }

    def tearDown(self):
        Recruiter.objects.all().delete()
        get_user_model().objects.all().delete()

    def test_create_recruiter_anonymous_user(self):
        """tests creating a recruiter profile by an anonymous user"""
        response = self.client.post('/api/v1/users/recruiters/',
                                    self.valid_payload,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recruiter.objects.count(), 2)
        recruiter = Recruiter.objects.get(id=response.data['id'])
        self.assertEqual(recruiter.user.email, self.valid_payload['user']['email'])
        self.assertEqual(recruiter.organization.name, self.valid_payload['organization']['name'].lower())
        self.assertEqual(recruiter.job_title, self.valid_payload['job_title'])
        self.assertEqual(recruiter.phone_number, self.valid_payload['phone_number'])

    def test_create_recruiter_existing_user(self):
        """tests creating a new recruiter profile when the user already exists"""
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/v1/users/recruiters/',
                                    self.invalid_payload,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Recruiter.objects.count(), 1)

    def test_create_existing_recruiter(self):
        """tests creating a recruiter profile when the recruiter already exists"""
        client = APIClient()
        client.force_authenticate(user=self.recruiter.user)
        response = client.post('/api/v1/users/recruiters/',
                               self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Recruiter.objects.count(), 1)

    def test_retrieve_recruiter(self):
        """tests retrieving a recruiter profile"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/v1/users/recruiters/{self.recruiter.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_recruiters(self):
        """tests listing recruiter profiles"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/users/recruiters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
