# Generated by Django 3.2.12 on 2022-03-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='bill_to',
            field=models.CharField(max_length=150),
        ),
    ]
