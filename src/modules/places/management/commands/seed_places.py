from django.core.management.base import BaseCommand
from modules.places.factories import PlaceFactory

class Command(BaseCommand):
    help = 'Seeds the database with places.'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help='The number of places to create.', default=10)

    def handle(self, *args, **options):
        number = options['number']
        for _ in range(number):
            PlaceFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {number} places.'))
