from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class NewsFilter(FilterSet):
    time_create__gt = DateTimeFilter(
        field_name='time_create', 
        lookup_expr='gte',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'content': ['icontains'],
        }