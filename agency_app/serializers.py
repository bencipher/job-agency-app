from rest_framework import serializers

from agency_app.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def validate_rate(self, value):
        if value < 0:
            raise serializers.ValidationError('Rate must be non-negative')
        return value


# # For validating requests
# class GetJobQueryParamsSerializer(serializers.Serializer):
#     perPage = serializers.IntegerField(min_value=1, max_value=100, default=10)
#     page = serializers.IntegerField(min_value=1, default=1)
#     sortBy = serializers.ChoiceField(choices=[
#         ('datePosted', 'Date Posted'), ('rate', 'Rate')], default='datePosted')
#     contractType = serializers.ChoiceField(
#         choices=[('contract', 'Contract'), ('permanent', 'Permanent')], required=False)
#     dateSincePosted = serializers.DateField(required=False)
#
#     def validate(self, data):
#         if data['perPage'] < 1 or data['perPage'] > 100:
#             raise serializers.ValidationError({'perPage': 'Must be between 1 and 100'})
#         if data['page'] < 1:
#             raise serializers.ValidationError({'page': 'Must be greater than or equal to 1'})
#         return data
