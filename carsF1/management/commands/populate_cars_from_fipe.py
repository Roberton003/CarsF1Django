from django.core.management.base import BaseCommand
from carsF1.models import Car, Brand, FipePrice
from carsF1 import gemini_service
import re
import time

class Command(BaseCommand):
    help = 'Populates the Car table from the FIPE data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate cars from FIPE data...'))

        # Clear existing Car data
        self.stdout.write(self.style.WARNING('Cleaning existing Car data...'))
        Car.objects.all().delete()
        Brand.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing Car data cleaned.'))

        for fipe_price in FipePrice.objects.all():
            fipe_year = fipe_price.fipe_year
            fipe_model = fipe_year.model
            fipe_brand = fipe_model.brand

            # Get or create the Brand
            brand, _ = Brand.objects.get_or_create(name=fipe_brand.name)

            # Extract year from FipeYear name
            year_match = re.search(r'(\d{4})', fipe_year.name)
            year = int(year_match.group(1)) if year_match else None

            # Create the Car
            car = Car.objects.create(
                model=fipe_model.name,
                brand=brand,
                factory_year=year,
                model_year=year,
                value=fipe_price.value
            )
            self.stdout.write(f'  Created car: {fipe_model.name} {year}')

            # Generate bio for the car
            self.stdout.write(f'Gerando bio para o carro: {car.model, car.brand, car.factory_year}')
            car.bio = gemini_service.generate_car_bio(car)
            car.save()
            self.stdout.write(f'  Bio gerada para: {car.model}')
            time.sleep(5) # Add a delay to avoid hitting API rate limits

        self.stdout.write(self.style.SUCCESS('Successfully populated cars from FIPE data.'))