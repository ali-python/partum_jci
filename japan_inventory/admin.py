from django.contrib import admin
<<<<<<< HEAD
from japan_inventory.models import CarBrand	, StockIn, StockOut, CarBuyPart
=======
from japan_inventory.models import CarBrand	, StockIn, StockOut, Expense, Employee
>>>>>>> master


class CarBrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_name', 'date'
    )


class StockInAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'car_brand', 'chasis_number', 'engine_number', 'car_model','buying_price',
         'dated'
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

<<<<<<< HEAD
class CarBuyPartAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'amount', 'date'
    )
=======

class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'amount', 'date'
    )


# ********* Start Admin of Employee *************
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'employee_name', 'employee_father_name', 'employee_cnic', 'employee_mobile'
    )

# *********** Ending Employee Admin **************

>>>>>>> master

admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(StockIn, StockInAdmin)
admin.site.register(StockOut, StockOutAdmin)
<<<<<<< HEAD
admin.site.register(CarBuyPart, CarBuyPartAdmin)

=======
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Employee, EmployeeAdmin)
>>>>>>> master

	