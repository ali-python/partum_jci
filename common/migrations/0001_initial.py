# Generated by Django 3.1.1 on 2020-11-25 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production', models.BooleanField(default=False)),
                ('demo', models.BooleanField(default=False)),
                ('local', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('admin', 'admin'), ('japan', 'japan'), ('pakistan', 'pakistan'), ('philippines', 'philippines')], default='admin', max_length=100)),
                ('address', models.TextField(blank=True, max_length=512, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=13, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=13, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
