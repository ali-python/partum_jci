from django import forms
from pak_inventory.models import (
    CarBrand, StockIn, StockOut, CarBuyPart, Expense, Employee, EmployeeSalary, Customer, Invoice,
    CustomerLedger, Bank, BankLedger, CarPartsInvoice, CarPartsStockOut
)


######## Bank###########
class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

class BankLedgerForm(forms.ModelForm):
    class Meta:
        model = BankLedger
        fields = '__all__'
################# end bank#####################


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


# ********** starting Employee Salary Forms ****************
class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'
# *********** ending Employee Salary Forms****************

# ************ Starting Customer Forms **************
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerLedgerForm(forms.ModelForm):
    class Meta:
        model = CustomerLedger
        fields = '__all__'
# *********** Ending Customer Forms *****************


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class CarPartsInvoiceForm(forms.ModelForm):
    class Meta:
        model = CarPartsInvoice
        fields = '__all__'


class CarPartsStockoutForm(forms.ModelForm):
    class Meta:
        model = CarPartsStockOut
        fields = '__all__'