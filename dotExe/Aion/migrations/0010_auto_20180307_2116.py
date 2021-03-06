# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0009_auto_20180307_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('1', 'Digital Watch'), ('0', 'Analog Watch'), ('2', 'Smart Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('1', 'Product Manager'), ('2', 'Accounting Manager'), ('0', 'Administrator'), ('3', 'Regular User')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
