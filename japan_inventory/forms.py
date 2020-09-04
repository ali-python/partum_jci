from django import forms
from japan_inventory.models import Expense


# ********** starting Expense Forms ****************
class ExpenseFormView(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
# *********** ending Expense Forms****************
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
