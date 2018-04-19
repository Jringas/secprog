from django.contrib import admin

# Register your models here.
from .models import User
admin.site.register(User)
from .models import User_Info 
admin.site.register(User_Info)
from .models import Product
admin.site.register(Product)
from .models import Product_Review
admin.site.register(Product_Review)
from .models import Transaction
admin.site.register(Transaction)
from .models import Transaction_Extension
admin.site.register(Transaction_Extension)
from .models import Common_Passwords
admin.site.register(Common_Passwords)
from .models import Common_Usernames
admin.site.register(Common_Usernames)