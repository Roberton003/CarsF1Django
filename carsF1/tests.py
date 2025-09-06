
from django.test import TestCase
from .models import Car, Brand, CarInventory

class CarInventorySignalTest(TestCase):

    def test_inventory_lifecycle(self):
        # Garante que o estado inicial é limpo
        CarInventory.objects.all().delete()
        self.assertEqual(CarInventory.objects.count(), 0)

        # Cria uma marca
        brand = Brand.objects.create(name='Test Brand')

        # 1. Cria o primeiro carro
        Car.objects.create(model='Car 1', brand=brand, value=100)
        
        # Verifica o inventário
        self.assertEqual(CarInventory.objects.count(), 1)
        inventory = CarInventory.objects.first()
        self.assertEqual(inventory.cars_count, 1)
        self.assertEqual(inventory.cars_value, 100)

        # 2. Cria o segundo carro
        Car.objects.create(model='Car 2', brand=brand, value=200)

        # Verifica a atualização do inventário
        self.assertEqual(CarInventory.objects.count(), 1) # Continua sendo 1 registro
        inventory.refresh_from_db()
        self.assertEqual(inventory.cars_count, 2)
        self.assertEqual(inventory.cars_value, 300)

        # 3. Deleta um carro
        Car.objects.get(model='Car 1').delete()

        # Verifica a atualização do inventário
        self.assertEqual(CarInventory.objects.count(), 1)
        inventory.refresh_from_db()
        self.assertEqual(inventory.cars_count, 1)
        self.assertEqual(inventory.cars_value, 200)
