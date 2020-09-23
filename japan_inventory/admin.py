from django.contrib import admin
from japan_inventory.models import CarBrand	, StockIn, StockOut, Expense, Employee, CarBuyPart, Customer, Invoice, CustomerLedger


class CarBrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_name', 'date'
    )


class StockInAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'status', 'car_brand', 'chasis_number', 'engine_number', 'car_model','buying_price',
         'dated', 'status_car'
    )

    @staticmethod
    def car_brand(obj):
        return obj.CarBrand.brand_name

class StockOutAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'car', 'sale_price', 'country', 'dated'
    )

    @staticmethod
    def car_brand(obj):
        return obj.StockOut.car_brand

class CarBuyPartAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'amount', 'date'
    )

class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'amount', 'date'
    )


# ********* Start Admin of Employee *************
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'employee_name', 'employee_father_name', 'employee_cnic', 'employee_mobile'
    )
    search_fields = (
        'employee_name', 'employee_cnic',
    )

    @staticmethod
    def employee_name(obj):
        return obj.employee_name
# *********** Ending Employee Admin **************


# ************* Starting Customer Admin **************
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'father_name', 'cnic', 'mobile', 'address', 'city', 'date'
    )

class CustomerLedgerAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'invoice', 'debit_amount', 'credit_amount', 'details', 'date'
    )
# ************* Ending Customer Admin *****************

class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'customer', 'country', 'bill_no', 'total_quantity', 'sub_total', 'paid_amount', 'remaining_payment',
        'discount', 'shipping', 'grand_total', 'cash_payment', 'cash_returned', 'date'
    )


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(StockIn, StockInAdmin)
admin.site.register(StockOut, StockOutAdmin)
admin.site.register(CarBuyPart, CarBuyPartAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)

	