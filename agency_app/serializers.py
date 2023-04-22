from rest_framework import serializers

from agency_app.models import Job


class JobSerializer(serializers.ModelSerializer):
    recruiter = ''
    applicant = ''

    class Meta:
        model = Job
        fields = '__all__'

    def validate_rate(self, value):
        if value < 0:
            raise serializers.ValidationError('Rate must be non-negative')
        return value
