# Generated by Django 3.2.5 on 2021-07-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0008_car_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total', models.PositiveIntegerField(blank=True)),
                ('total_price', models.PositiveIntegerField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('cars', models.ManyToManyField(to='cars.Car')),
            ],
        ),
    ]
