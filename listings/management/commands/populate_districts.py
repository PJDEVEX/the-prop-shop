from django.core.management.base import BaseCommand
from listings.models import City, District
from listings.addresses_choices import district_dict


class Command(BaseCommand):
    help = 'Populate districts'

    def handle(self, *args, **kwargs):
        # Extract district names and codes from district_dict
        district_data = [(district_code, district_name) for district_name, district_code in district_dict.items()]

        # Create or update districts
        for district_code, district_name in district_data:
            district, created = District.objects.get_or_create(name=district_name)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created district: {district_name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'District already exists: {district_name}'))
