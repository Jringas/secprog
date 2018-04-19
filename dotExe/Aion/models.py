from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.validators import EmailValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from passlib.hash import pbkdf2_sha256
# Create your models here.
privilege_level = {
    ('0', 'Administrator'),
    ('1', 'Product Manager'),
    ('2', 'Accounting Manager'),
    ('3', 'Regular User')
}

watch_type = {
    ('0', 'Analog Watch'),
    ('1', 'Digital Watch'),
    ('2', 'Smart Watch')
}

watch_rating = { 
    ('1', '1 Star'),
    ('2', '2 Star'),
    ('3', '3 Star'),
    ('4', '4 Star'),
    ('5', '5 Star'),
}

class User(models.Model):
    user_username = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_privilege = models.CharField(max_length=16, choices=privilege_level , default='3')
    user_first_name = models.CharField(max_length=200)
    user_last_name = models.CharField(max_length=200)
    user_middle_initial = models.CharField(max_length=3)
    user_email = models.EmailField(blank=False, null=True, max_length=200, validators=[EmailValidator(message='Invalid Email!')])
#    user_thumbnail = models.ImageField(blank=True, null=True, upload_to='Product/')
    user_pass_tries = models.PositiveIntegerField(blank=True, null=True, default=0)
    user_is_active = models.BooleanField(default=True)
    
    def verify_password(self, input_pass):
        return pbkdf2_sha256.verify(input_pass, self.user_password)
    
    def __str__(self):
        return self.user_username
    

    
class User_Info(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    billing_house_number = models.CharField(blank=True, null=True, max_length=200)
    billing_street = models.CharField(blank=True, null=True, max_length=200)
    billing_subdivision = models.CharField(blank=True, null=True, max_length=200)
    billing_city = models.CharField(blank=True, null=True, max_length=200)
    billing_postal_code = models.PositiveIntegerField(blank=True, null=True)
    billing_country = models.CharField(blank=True, null=True, max_length=200)
    shipping_house_number = models.CharField(blank=True, null=True, max_length=200)
    shipping_street = models.CharField(blank=True, null=True, max_length=200)
    shipping_subdivision = models.CharField(blank=True, null=True, max_length=200)
    shipping_city = models.CharField(blank=True, null=True, max_length=200)
    shipping_postal_code = models.PositiveIntegerField(blank=True, null=True)
    shipping_country = models.CharField(blank=True, null=True, max_length=200)
    
    def __str__(self):
        return self.user_id.user_username

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_quantity = models.IntegerField(default=0)
    product_price = models.FloatField(default=0)
    product_rating = models.CharField(max_length=16, choices=watch_rating, default='3')
#    product_thumbnail = models.ImageField(blank=True, null=True, upload_to='Product/')
    product_type = models.CharField(max_length=16, choices=watch_type, default='0')
    product_bought = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product_name
    
class Product_Review(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    product_user_review = models.ForeignKey(User, on_delete = models.CASCADE)
    product_comment = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.product_id.product_name

class Transaction(models.Model):
    transaction_user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    transaction_quantity = models.IntegerField(default=0)
    transaction_order_total = models.FloatField(default=0)
    transaction_date = models.DateTimeField(default=datetime.now)
    
class Transaction_Extension(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    transaction_total = models.FloatField(default=0)
    
    def __str__(self):
        return self.product_id.product_name

class Common_Passwords(models.Model):
    password = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.password
    
class Common_Usernames(models.Model):
    usernames = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.usernames