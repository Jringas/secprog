# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-12 12:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0029_auto_20180312_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.CharField(choices=[('4', '4 Star'), ('3', '3 Star'), ('5', '5 Star'), ('1', '1 Star'), ('2', '2 Star')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('0', 'Analog Watch'), ('1', 'Digital Watch'), ('2', 'Smart Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('0', 'Administrator'), ('2', 'Accounting Manager'), ('3', 'Regular User'), ('1', 'Product Manager')], default='3', max_length=16),
        ),
    ]