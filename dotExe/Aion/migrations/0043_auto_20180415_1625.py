# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-15 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0042_auto_20180415_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.CharField(choices=[('3', '3 Star'), ('5', '5 Star'), ('2', '2 Star'), ('4', '4 Star'), ('1', '1 Star')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('0', 'Analog Watch'), ('1', 'Digital Watch'), ('2', 'Smart Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('3', 'Regular User'), ('1', 'Product Manager'), ('0', 'Administrator'), ('2', 'Accounting Manager')], default='3', max_length=16),
        ),
    ]
