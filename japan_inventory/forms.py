from django import forms
from japan_inventory.models import Expense


# ********** starting Expense Forms ****************
class ExpenseFormView(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
# *********** ending Expense Forms****************