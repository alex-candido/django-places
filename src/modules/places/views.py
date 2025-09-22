from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter
from .models import Place
from .serializers import PlaceSerializer
from .filters import PlaceFilter

class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = StandardResultsPagination
    filter_backends = [InBBoxFilter, DistanceToPointFilter, DjangoFilterBackend]
    filterset_class = PlaceFilter
    bbox_filter_field = 'location'
    distance_filter_field = 'location'
