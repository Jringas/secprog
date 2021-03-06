# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aion', '0017_auto_20180308_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='Product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('0', 'Analog Watch'), ('2', 'Smart Watch'), ('1', 'Digital Watch')], default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_privilege',
            field=models.CharField(choices=[('2', 'Accounting Manager'), ('0', 'Administrator'), ('1', 'Product Manager'), ('3', 'Regular User')], default='3', max_length=16),
        ),
    ]
