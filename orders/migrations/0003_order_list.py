# Generated by Django 3.2.5 on 2021-07-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210724_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total', models.PositiveIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveIntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
