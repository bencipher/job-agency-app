from rest_framework import serializers

from users.models import Applicant, CustomUser, Organization, Recruiter


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'address', 'phone_number']


class RecruiterSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = Recruiter
        fields = ['id', 'user', 'organization', 'job_title', 'phone_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        recruiter = Recruiter.objects.create(user=user, **validated_data)
        return recruiter


class ApplicantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Applicant
        fields = ['id', 'user', 'technology_stack', 'expected_salary',
                  'hourly_rate', 'resume', 'address', 'city',
                  'state', 'zip_code']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        applicant = Applicant.objects.create(user=user, **validated_data)
        return applicant
