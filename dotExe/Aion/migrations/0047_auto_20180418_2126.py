# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-18 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0046_auto_20180418_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.CharField(choices=[('2', '2 Star'), ('5', '5 Star'), ('4', '4 Star'), ('3', '3 Star'), ('1', '1 Star')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('2', 'Smart Watch'), ('1', 'Digital Watch'), ('0', 'Analog Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('1', 'Product Manager'), ('0', 'Administrator'), ('2', 'Accounting Manager'), ('3', 'Regular User')], default='3', max_length=16),
        ),
    ]
