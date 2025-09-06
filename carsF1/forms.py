from django import forms
from carsF1.models import Car 

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000,00 ')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None and factory_year < 1975:
            self.add_error('factory_year', 'Ano de fabricação mínimo deve ser de 1975')
        return factory_year
