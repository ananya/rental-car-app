# Generated by Django 2.2.2 on 2019-06-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRent', '0004_auto_20190606_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_Type',
            field=models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Mini SUV', 'Mini SUV')], max_length=10),
        ),
    ]
