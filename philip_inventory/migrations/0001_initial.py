# Generated by Django 3.1.1 on 2020-11-30 19:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('Branch', models.CharField(blank=True, max_length=500, null=True)),
                ('account_number', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarBuyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarPartsInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('bill_no', models.CharField(blank=True, max_length=10, null=True)),
                ('total_quantity', models.CharField(blank=True, default=1, max_length=10, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('remaining_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('cash_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('cash_returned', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('cnic', models.CharField(max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(blank=True, max_length=500, null=True)),
                ('employee_father_name', models.CharField(blank=True, max_length=500, null=True)),
                ('employee_cnic', models.CharField(blank=True, max_length=500, null=True)),
                ('employee_mobile', models.CharField(blank=True, max_length=500, null=True)),
                ('employee_address', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('bill_no', models.CharField(blank=True, max_length=10, null=True)),
                ('total_quantity', models.CharField(blank=True, default=1, max_length=10, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('remaining_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('cash_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('cash_returned', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_sales', to='philip_inventory.customer')),
            ],
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chasis_number', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_number', models.CharField(blank=True, max_length=100, null=True)),
                ('car_model', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('buying_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('car_name', models.CharField(blank=True, max_length=100, null=True)),
                ('status_car', models.BooleanField(default=True)),
                ('dated', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('car_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_brand_name', to='philip_inventory.carbrand')),
            ],
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('country', models.CharField(choices=[('japan', 'japan'), ('philipines', 'philipines'), ('pakistan', 'pakistan')], default='japan', max_length=100)),
                ('dated', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_stockout', to='philip_inventory.stockin')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_stockout', to='philip_inventory.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_salary', to='philip_inventory.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLedger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('credit_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('details', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_ledger', to='philip_inventory.customer')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_ledger', to='philip_inventory.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='CarPartsStockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('stock_out_quantity', models.CharField(blank=True, default=1, max_length=10, null=True)),
                ('country', models.CharField(choices=[('japan', 'japan'), ('philipines', 'philipines'), ('pakistan', 'pakistan')], default='pakistan', max_length=100)),
                ('dated', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('car_parts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_parts_stockout', to='philip_inventory.carbuypart')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_car_parts_stockout', to='philip_inventory.carpartsinvoice')),
            ],
        ),
        migrations.AddField(
            model_name='carpartsinvoice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_sales_car_parts', to='philip_inventory.customer'),
        ),
        migrations.CreateModel(
            name='BankLedger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('credit_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('details', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_ledger', to='philip_inventory.bank')),
            ],
        ),
    ]
