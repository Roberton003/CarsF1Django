from django.contrib import admin
from carsF1.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model','brand')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)