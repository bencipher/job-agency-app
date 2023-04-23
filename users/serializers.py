from django.db import transaction
from rest_framework import serializers

from users.models import Applicant, CustomUser, Organization, Recruiter


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


class OrganizationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Organization
        fields = ['name', 'address']


class RecruiterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(required=False, view_name='recruiter-detail')
    organization = OrganizationSerializer()
    user = CustomUserSerializer()

    class Meta:
        model = Recruiter
        fields = ['user', 'organization', 'job_title', 'phone_number', 'url']

    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop('user')
            organization_data = validated_data.pop('organization')
            user_password = user_data.pop('password')
            user, created = CustomUser.objects.get_or_create(email=user_data['email'], defaults=user_data)
            user.set_password(user_password)
            organization_name = organization_data['name']
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

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        organization_data = validated_data.pop('organization')

        if user_data:
            user = instance.user
            user.email = user_data.get('email', user.email)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.save()

        organization = instance.organization
        organization.name = organization_data.get('name', organization.name)
        organization.address = organization_data.get('address', organization.address)
        organization.phone_number = organization_data.get('phone_number', organization.phone_number)
        organization.save()

        instance.is_owner = validated_data.get('is_owner', instance.is_owner)
        instance.save()

        return instance


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
