# Generated by Django 3.1.1 on 2020-09-02 08:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chasis_number', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('engine_number', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('model', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('dated_order', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('car_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_brand_name', to='japan_inventory.carbrand')),
            ],
        ),
    ]