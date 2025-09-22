import django_filters
from .models import Place

class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'name': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith'],
            'description': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith'],
            'address': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith'],
            'city': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith'],
            'state': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith'],
            'country': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith'],
            
            'status': ['exact', 'in'], 
            'type': ['exact', 'in'],
            
            'created_at': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'updated_at': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }