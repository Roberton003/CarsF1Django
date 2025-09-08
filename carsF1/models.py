from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Nome')

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'


class FipeBrand(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=20) # 'carros', 'motos', 'caminhoes'

    def __str__(self):
        return f'{self.name} ({self.vehicle_type})'


class FipeModel(models.Model):
    brand = models.ForeignKey(FipeBrand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    class Meta:
        unique_together = ('brand', 'code')

    def __str__(self):
        return f'{self.brand.name} - {self.name}'


class FipeYear(models.Model):
    model = models.ForeignKey(FipeModel, on_delete=models.CASCADE, related_name='years')
    name = models.CharField(max_length=100) # e.g., "2000 Gasolina"
    code = models.CharField(max_length=50) # e.g., "2000-1"

    class Meta:
        unique_together = ('model', 'code')

    def __str__(self):
        return f'{self.model.name} - {self.name}'


class FipePrice(models.Model):
    fipe_year = models.ForeignKey(FipeYear, on_delete=models.CASCADE, related_name='prices')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    reference_month = models.CharField(max_length=100) # e.g., "setembro de 2025"
    fipe_code = models.CharField(max_length=50)
    consultation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('fipe_year', 'reference_month')

    def __str__(self):
        return f'{self.fipe_year.name} - R$ {self.value}'
