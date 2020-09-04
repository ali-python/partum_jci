from django import forms
from .models import (CarBrand, StockIn, StockOut)

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'

class StockInForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = '__all__'

class StockOutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = '__all__'

