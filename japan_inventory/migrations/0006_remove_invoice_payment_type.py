# Generated by Django 3.1.1 on 2020-09-09 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japan_inventory', '0005_invoice_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payment_type',
        ),
    ]
