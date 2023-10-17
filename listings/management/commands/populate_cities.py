from django.core.management.base import BaseCommand
from listings.models import City, District
from listings.addresses_choices import city_dict


class Command(BaseCommand):
    help = 'Populate cities and districts'

    def handle(self, *args, **kwargs):
        for city_name, city_data in city_dict.items():
            district_name = city_data['district']
            postal_code = city_data['postal_code']

            # Create or get the district
            district, created = District.objects.get_or_create(name=district_name)

            # Create the city
            city, created = City.objects.get_or_create(
                name=city_name,
                district=district,
                postal_code=postal_code
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created {city}'))

# Management command to populate the cities and districts:
# python manage.py populate_cities
