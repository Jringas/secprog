# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0016_auto_20180308_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('2', 'Smart Watch'), ('0', 'Analog Watch'), ('1', 'Digital Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('0', 'Administrator'), ('3', 'Regular User'), ('1', 'Product Manager'), ('2', 'Accounting Manager')], default='3', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Product/'),
        ),
    ]
