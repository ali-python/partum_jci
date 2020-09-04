from django import forms
from .models import (CarBrand, StockIn, StockOut, CarBuyPart, Expense, Employee)


# ********** starting Expense Forms ****************
class ExpenseFormView(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
# *********** ending Expense Forms****************

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

class CarBuyPartForm(forms.ModelForm):
    class Meta:
        model = CarBuyPart
        fields = '__all__'


# ********** starting Employee Forms ****************
class EmployeeFormView(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
# *********** ending Employee Forms****************