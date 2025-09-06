from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from carsF1.models import Car, CarInventory

def car_inventory_update():
    cars_count = Car.objects.all().count()
    total_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] or 0

    inventory = CarInventory.objects.first()
    if inventory:
        inventory.cars_count = cars_count
        inventory.cars_value = total_value
        inventory.save()
    else:
        CarInventory.objects.create(
            cars_count=cars_count,
            cars_value=total_value
        )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
