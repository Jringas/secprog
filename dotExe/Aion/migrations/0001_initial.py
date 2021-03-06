# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_price', models.IntegerField(default=0)),
                ('product_rating', models.IntegerField(default=0)),
                ('product_thumbnail', models.ImageField(blank=True, null=True, upload_to='productPhoto/')),
                ('product_type', models.CharField(choices=[('2', 'Smart Watch'), ('1', 'Digital Watch'), ('0', 'Analog Watch')], default='0', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_comment', models.CharField(blank=True, max_length=300, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aion.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_order_total', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aion.Product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_username', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
                ('user_privilege', models.CharField(choices=[('0', 'Administrator'), ('2', 'Accounting Manager'), ('1', 'Product Manager'), ('3', 'Regular User')], default='3', max_length=16)),
                ('user_first_name', models.CharField(max_length=200)),
                ('user_last_name', models.CharField(max_length=200)),
                ('user_middle_initial', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_house_number', models.CharField(blank=True, max_length=200, null=True)),
                ('billing_street', models.CharField(blank=True, max_length=200, null=True)),
                ('billing_subdivision', models.CharField(blank=True, max_length=200, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=200, null=True)),
                ('billing_postal_code', models.CharField(blank=True, max_length=200, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_house_number', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_street', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_subdivision', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_postal_code', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_country', models.CharField(blank=True, max_length=200, null=True)),
                ('user_email', models.CharField(blank=True, max_length=200, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aion.User')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aion.User'),
        ),
        migrations.AddField(
            model_name='product_review',
            name='product_user_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aion.User'),
        ),
    ]
