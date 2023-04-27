from django.db import transaction
from rest_framework import serializers

from users.models import Applicant, CustomUser, Organization, Recruiter


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name']

    def get_validation_exclusions(self, instance=None):
        exclusions = super().get_validation_exclusions(instance)
        exclusions.append('email')
        exclusions.append('password')
        return exclusions


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(required=False, view_name='organization-detail')

    class Meta:
        model = Organization
        fields = ['id', 'name', 'address', 'url']

    def update(self, instance, validated_data):
        organization = instance
        organization.name = validated_data.get('name', organization.name)
        organization.address = validated_data.get('address', organization.address)
        organization.save()
        return super().update(organization, validated_data)


class RecruiterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['job_title', 'phone_number']


class RecruiterSwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['id', 'user', 'organization', 'job_title', 'phone_number', 'url']


class RecruiterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(required=False, view_name='recruiter-detail')
    organization = OrganizationSerializer(required=False)
    user = CustomUserSerializer(required=False)

    class Meta:
        model = Recruiter
        fields = ['id', 'user', 'organization', 'job_title', 'phone_number', 'url']

    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop('user')
            organization_data = validated_data.pop('organization')
            user_password = user_data.pop('password')
            user, created = CustomUser.objects.get_or_create(email=user_data['email'], defaults=user_data)
            user.set_password(user_password)
            user.save()
            organization_name = organization_data['name'].strip().lower()
            organization, created = Organization.objects.get_or_create(name=organization_name)
            if created:
                organization.address = organization_data.get('address')
                organization.save()
            recruiter = Recruiter.objects.create(user=user, organization=organization, **validated_data)
            recruiter.organization = organization
            recruiter.is_owner = created
            recruiter.save()

            organization.owner = recruiter
        return recruiter


class ApplicantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    url = serializers.HyperlinkedIdentityField(required=False, view_name='applicant-detail')

    class Meta:
        model = Applicant
        fields = ['id', 'user', 'technology_stack', 'expected_salary',
                  'hourly_rate', 'resume', 'address', 'city',
                  'state', 'zip_code', 'url']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        applicant = Applicant.objects.create(user=user, **validated_data)
        return applicant
