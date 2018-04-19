# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-12 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0028_auto_20180312_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.CharField(choices=[('5', '5 Star'), ('2', '2 Star'), ('3', '3 Star'), ('4', '4 Star'), ('1', '1 Star')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('0', 'Analog Watch'), ('2', 'Smart Watch'), ('1', 'Digital Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('1', 'Product Manager'), ('3', 'Regular User'), ('2', 'Accounting Manager'), ('0', 'Administrator')], default='3', max_length=16),
        ),
    ]
