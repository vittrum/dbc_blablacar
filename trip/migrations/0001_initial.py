# Generated by Django 3.1.5 on 2021-01-23 16:04

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
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('departure_date', models.DateField(blank=True)),
                ('departure_time', models.TimeField(blank=True)),
                ('places_available', models.IntegerField(blank=True)),
                ('status', models.CharField(default='trip_status', max_length=100)),
            ],
            options={
                'db_table': 'trips',
            },
        ),
        migrations.CreateModel(
            name='TripComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('type', models.CharField(default='comment', max_length=30)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'trips_comments',
            },
        ),
        migrations.CreateModel(
            name='CityTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='departure_city', to='trip.city')),
                ('destination_city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='trip.city')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.trip')),
            ],
            options={
                'db_table': 'trips_cities',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baggage_volume', models.IntegerField(blank=True)),
                ('status', models.CharField(default='car_status', max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=30)),
                ('places_count', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
