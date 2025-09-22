import uuid

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Status(models.IntegerChoices):
    ACTIVE = 1, 'Active'
    INACTIVE = 0, 'Inactive'
    
class PlaceType(models.IntegerChoices):
    BAR = 0, 'Bar'
    PUB = 1, 'Pub'
    RESTAURANT = 2, 'Restaurant'
    CAFE = 3, 'Cafe'
    NIGHTCLUB = 4, 'Nightclub'
    BREWERY = 5, 'Brewery'
    WINERY = 6, 'Winery'
    FOOD_TRUCK = 7, 'Food Truck'
    COCKTAIL_BAR = 8, 'Cocktail Bar'
    SPORTS_BAR = 9, 'Sports Bar'
    LOUNGE = 10, 'Lounge'
    ROOFTOP_BAR = 11, 'Rooftop Bar'

class Place(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    location = models.PointField(srid=4326, geography=True)
    
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    type = models.IntegerField(choices=PlaceType.choices, default=PlaceType.BAR)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
      
    def set_location(self, lat: float, lng: float):
        self.location = Point(lng, lat, srid=4326)