# Generated by Django 3.1.1 on 2020-09-02 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japan_inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockin',
            old_name='model',
            new_name='car_model',
        ),
    ]