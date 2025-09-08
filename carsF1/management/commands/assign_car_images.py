import os
import re
from django.core.management.base import BaseCommand
from django.core.files import File
from carsF1.models import Car

class Command(BaseCommand):
    help = 'Assigns images from media/cars/ to corresponding Car objects.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to assign car images...'))

        media_cars_dir = 'media/cars/'
        
        # Ensure the directory exists
        if not os.path.exists(media_cars_dir):
            self.stdout.write(self.style.ERROR(f'Directory {media_cars_dir} does not exist.'))
            return

        for filename in os.listdir(media_cars_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
                # Extract car model and year from filename (e.g., "Strada (2023).jpeg")
                # This is a simplified parsing and might need refinement based on actual filenames
                name_parts = os.path.splitext(filename)[0].split(' (')
                if len(name_parts) == 2:
                    model_name = name_parts[0].strip()
                    year_str = name_parts[1].replace(')', '').strip()
                    try:
                        year = int(year_str)
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f'Could not parse year from filename: {filename}. Skipping.'))
                        continue
                elif len(name_parts) == 1: # Handle cases like Hilux2023.jpeg
                    model_name_match = re.match(r'([a-zA-Z]+)(\d{4})', name_parts[0])
                    if model_name_match:
                        model_name = model_name_match.group(1)
                        year = int(model_name_match.group(2))
                    else:
                        self.stdout.write(self.style.WARNING(f'Could not parse model and year from filename: {filename}. Skipping.'))
                        continue
                else:
                    self.stdout.write(self.style.WARNING(f'Filename format not recognized: {filename}. Skipping.'))
                    continue

                try:
                    # Find the corresponding Car object
                    car = Car.objects.get(model__exact=model_name, factory_year=year)

                    # Open the image file and assign it to the Car object's photo field
                    with open(os.path.join(media_cars_dir, filename), 'rb') as f:
                        car.photo.save(filename, File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Successfully assigned {filename} to {car.model} ({car.factory_year}).'))

                except Car.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Car not found for {model_name} ({year}). Skipping {filename}.'))
                except Car.MultipleObjectsReturned:
                    self.stdout.write(self.style.WARNING(f'Multiple cars found for {model_name} ({year}). Skipping {filename}.'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error processing {filename}: {e}'))

        self.stdout.write(self.style.SUCCESS('Image assignment process completed.'))
