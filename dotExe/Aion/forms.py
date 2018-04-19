from django import forms
from .models import Product
from .models import User
from django.core.validators import validate_email

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_quantity', 'product_price', 'product_rating', 'product_type']
#    	fields = ['product_name', 'product_quantity', 'product_price', 'product_rating', 'product_thumbnail', 'product_type']

class AdminUserImageForm(forms.ModelForm):

    user_password = forms.CharField(widget=forms.PasswordInput)	
    class Meta:
        model = User
#    	fields = ['user_username', 'user_password', 'user_privilege', 'user_first_name', 'user_last_name', 'user_middle_initial', 'user_email', 'user_thumbnail']
        fields = ['user_username', 'user_password', 'user_privilege', 'user_first_name', 'user_last_name', 'user_middle_initial', 'user_email']
    
class EditProfileForm(forms.ModelForm):
	
    user_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
#    	fields = ['user_username', 'user_password', 'user_first_name', 'user_last_name', 'user_middle_initial', 'user_email', 'user_thumbnail']
        fields = ['user_username', 'user_password', 'user_first_name', 'user_last_name', 'user_middle_initial', 'user_email']