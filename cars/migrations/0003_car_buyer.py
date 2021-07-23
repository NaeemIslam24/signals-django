# Generated by Django 3.2.5 on 2021-07-23 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0005_buyer'),
        ('cars', '0002_remove_car_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buyers.buyer'),
            preserve_default=False,
        ),
    ]
