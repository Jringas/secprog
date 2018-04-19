# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-18 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0045_auto_20180415_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_pass_tries',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.CharField(choices=[('4', '4 Star'), ('5', '5 Star'), ('2', '2 Star'), ('3', '3 Star'), ('1', '1 Star')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('0', 'Analog Watch'), ('1', 'Digital Watch'), ('2', 'Smart Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('3', 'Regular User'), ('0', 'Administrator'), ('2', 'Accounting Manager'), ('1', 'Product Manager')], default='3', max_length=16),
        ),
    ]