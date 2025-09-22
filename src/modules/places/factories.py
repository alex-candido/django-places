import factory
from factory.django import DjangoModelFactory
from django.contrib.gis.geos import Point
from faker import Faker
from .models import Place, Status, PlaceType

fake = Faker()

class PlaceFactory(DjangoModelFactory):
    class Meta:
        model = Place

    name = factory.Faker('company')
    description = factory.Faker('text')
    address = factory.Faker('address')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    country = factory.Faker('country_code')
    
    location = factory.LazyFunction(lambda: Point(float(fake.longitude()), float(fake.latitude())))
    
    status = factory.Iterator([s.value for s in Status])
    type = factory.Iterator([t.value for t in PlaceType])