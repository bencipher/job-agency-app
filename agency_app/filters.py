from django_filters import CharFilter, DateFilter, FilterSet

from agency_app.models import Job


class JobFilter(FilterSet):
    contract_type = CharFilter(field_name='contract_type')
    date_since_posted = DateFilter(
        field_name='date_posted',
        lookup_expr='gte',
        method='filter_date_since_posted')

    class Meta:
        model = Job
        fields = ('contract_type', 'date_since_posted')
