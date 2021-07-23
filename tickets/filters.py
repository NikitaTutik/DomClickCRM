import django_filters
from django.forms import TextInput
from django_filters import DateFilter
from .models import Ticket


class TicketFilter(django_filters.FilterSet):
    date = DateFilter(field_name="date", lookup_expr="gte", label='Filter by date')
    startdate = DateFilter(field_name="date", lookup_expr="gte", label='Start date', widget=TextInput(attrs={'placeholder': 'MonthDayYear', 'class': 'full-width'}))
    enddate = DateFilter(field_name="date", lookup_expr="lte", label='End date',widget=TextInput(attrs={'placeholder': 'MonthDayYear', 'class': 'full-width'}))
    class Meta:
        model = Ticket
        fields = ('category', 'status', 'date')
