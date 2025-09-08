from django.db.models import Sum
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from carsF1.models import Car, CarInventory
from . import gemini_service


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

# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     # Se o carro é novo (ainda não tem um ID) e a bio está em branco...
#     if instance.pk is None and not instance.bio:
#         print(f"Gerando bio para o carro: {instance.model, instance.brand, instance.model_year}") # Log para depuração
#         # ...chama nosso serviço para gerar a bio.
#         instance.bio = gemini_service.generate_car_bio(instance)
     
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()