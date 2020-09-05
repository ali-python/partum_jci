from django.db import models
from django.utils import timezone

class CarBrand(models.Model):
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.brand_name


class StockIn(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='car_brand_name')
    chasis_number = models.DecimalField(max_digits=65, decimal_places=2, default=0,
                                         null=True, blank=True)
    engine_number = models.DecimalField(max_digits=65, decimal_places=2, default=0,
                                       null=True, blank=True)
    car_model = models.DecimalField(max_digits=65, decimal_places=2, default=0,
    									null=True, blank=True)
    buying_price = models.DecimalField(max_digits=65, decimal_places=2, default=0,
    									null=True, blank=True)
    colour = models.CharField(max_length=100, null=True, blank=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    dated = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return str(self.car_brand) if self.car_brand else ''


class StockOut(models.Model):
	COUNTRY_PAKISTAN = 'pakistan'
	COUNTRY_PHILIPINES = 'philipines'
	COUNTRY_JAPAN = 'japan'

	DISPATCH_COUNTRY = (
			(COUNTRY_JAPAN, 'japan'),
			(COUNTRY_PHILIPINES, 'philipines'),
			(COUNTRY_PAKISTAN, 'pakistan')
		)
	car = models.ForeignKey(StockIn, on_delete=models.CASCADE, null=True, blank=True,
							related_name='car_stockout')
	sale_price = models.DecimalField(max_digits=65, decimal_places=2, default=0,
									null=True, blank=True)
	country = models.CharField(
        max_length=100, choices=DISPATCH_COUNTRY, default= COUNTRY_JAPAN
    )
	dated = models.DateField(default=timezone.now, null=True, blank=True)

	def __str__(self):
		return self.country

class CarBuyPart(models.Model):
    description = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=65, decimal_places=2, default=0,
                                    null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.description

# ************ Starting Expense System Model ***************
class Expense(models.Model):
    description = models.TextField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return str(self.description)
# ************** Ending Expense System Model **************


# *************** Starting Employee Model ****************
class Employee(models.Model):
	employee_name = models.CharField(max_length=500, blank=True, null=True)
	employee_father_name = models.CharField(max_length=500, blank=True, null=True)
	employee_cnic = models.CharField(max_length=500, blank=True, null=True)
	employee_mobile = models.CharField(max_length=500, blank=True, null=True)
	employee_address = models.CharField(max_length=500, blank=True, null=True)

	def __str__(self):
		return self.employee_cnic
# ***************** Ending Employee Model ***********************


# *************** Starting Customer Model *********************
class Customer(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200, null=True, blank=True)
    cnic = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name
# ************** Ending Customer Model ********************