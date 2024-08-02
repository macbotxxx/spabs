import django_filters
from django import forms
from django_filters import DateFilter
from .models import JobEnrollment, Transactions


class JobENrollmentFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name="created_date__date",
        lookup_expr="gte",
        label="start date",
        widget=forms.DateInput(attrs={'type': 'date'})
        )

    end_date = DateFilter(
        field_name="created_date__date",
        lookup_expr="lte",
        label="end date",
        widget=forms.DateInput(attrs={'type': 'date'})
        )

    class Meta:
        model = JobEnrollment
        fields = ('names', 'phone_number')


class TransactionsFilter(django_filters.FilterSet):
    # Define a queryset for the dropdown choices

    class Meta:
        model = Transactions
        fields = [
            "job_aplicant",
            "payment_ref",
            "settled",
            ]
