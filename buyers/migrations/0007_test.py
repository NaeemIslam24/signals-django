# Generated by Django 3.2.5 on 2021-07-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0006_alter_buyer_from_singnal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10)),
                ('from_singnal', models.BooleanField(default=False)),
            ],
        ),
    ]
