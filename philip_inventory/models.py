from django.db import models
from django.utils import timezone
from django.db.models import Sum


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

    def get_unpaid_amount(self):
        customer_ledgers = self.customer_ledger.all()

        if customer_ledgers:
            ledger_debit = customer_ledgers.aggregate(Sum('debit_amount'))
            ledger_credit = customer_ledgers.aggregate(Sum('credit_amount'))

            debit_amount = ledger_debit.get('debit_amount__sum')
            credit_amount = ledger_credit.get('credit_amount__sum')
        else:
            debit_amount = 0
            credit_amount = 0

        unpaid_amount = debit_amount - credit_amount
        return unpaid_amount

# ************** Ending Customer Model ********************

####################### invoice model###########################

class Invoice(models.Model):

    PAYMENT_CASH = 'Cash'
    PAYMENT_CHECK = 'Check'

    PAYMENT_TYPES = (
        (PAYMENT_CASH, 'Cash'),
        (PAYMENT_CHECK, 'Check'),
    )
    country = models.CharField(max_length=200, blank=True, null=True)

    customer = models.ForeignKey(
        'Customer',
        related_name='customer_sales',
        blank=True, null=True, on_delete=models.SET_NULL
    )

    payment_type = models.CharField(choices=PAYMENT_TYPES, default=PAYMENT_CASH, max_length=100)

    bill_no = models.CharField(max_length=10, blank=True, null=True)

    total_quantity = models.CharField(
        max_length=10, blank=True, null=True, default=1
    )

    sub_total = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    paid_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    remaining_payment = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    discount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    shipping = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    grand_total = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    cash_payment = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )

    cash_returned = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return str(self.id).zfill(7)

class CustomerLedger(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_ledger'
    )
    invoice = models.ForeignKey(
        'Invoice', related_name='invoice_ledger', blank=True, null=True, on_delete=models.CASCADE
    )
    debit_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    credit_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    details = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.customer.name

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
    invoice = models.ForeignKey(
        'Invoice', related_name='invoice_stockout', blank=True, null=True, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=65, decimal_places=2, default=0,
                                    null=True, blank=True)
    country = models.CharField(
        max_length=100, choices=DISPATCH_COUNTRY, default= COUNTRY_JAPAN
    )
    dated = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.country
######################################## end invoice model #############################333
