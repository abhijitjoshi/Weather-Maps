# Generated by Django 2.1.4 on 2018-12-31 17:33

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.TextField()),
                ('destination', models.TextField()),
                ('travel_mode', models.TextField(default='driving')),
                ('routes_response', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('route_weather_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], null=True)),
                ('route_cities_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
