from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import User, User_Info, Product, Product_Review, Transaction, Transaction_Extension
from django.core.files.storage import FileSystemStorage
from Aion.forms import ProductImageForm, AdminUserImageForm, EditProfileForm
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta
import dateutil.parser
import re
import logging
# Create your views here.



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('dotExe.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    ssymbol_error = re.search(r"\W", password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    return password_ok

def logOut(request):
    watch_list = Product.objects.order_by('-id')
    context = {
		'watchList': watch_list,
	}

    if 'timeout' in request.session:
        context['timeout'] = True
        del request.session['timeout']
    request.session.flush()
    request.session['user'] = -1

    return render(request, 'Aion/homepage.html',context)

def error_404(request):
        data = {}
        return render(request,'Aion/404.html', data)

def error_500(request):
        data = {}
        return render(request,'Aion/500.html', data)

def managerTransactionPageOne(request):
    user = get_object_or_404(User, pk = request.session['user'])
    transaction_list = Transaction.objects.all()
    filter1 = 1
    total = 0.0
    for x in transaction_list:
        total = total + x.transaction_order_total
    content = {
        'user':user,
        'transaction':transaction_list,
        'filter': filter1,
        'total':total
    }
    return render(request, 'Aion/viewtransact.html', content)

def managerTransactionPageTwo(request):
    user = get_object_or_404(User, pk = request.session['user'])
    transaction_list = Transaction.objects.all()
    filter2 = 2
    analog_watch = []
    digital_watch = []
    smart_watch = []
    analog_list = Product.objects.filter(product_type='0')
    digital_list = Product.objects.filter(product_type='1')
    smart_list = Product.objects.filter(product_type='2')
    analog_total = 0
    digital_total = 0
    smart_total = 0
    for y in transaction_list:
        if y.product_id.product_type == '0':
            analog_total = analog_total + y.transaction_order_total
            analog_watch.append(y)
        elif y.product_id.product_type == '1':
            digital_total = digital_total + y.transaction_order_total
            digital_watch.append(y)
        else:
            smart_total = smart_total + y.transaction_order_total
            smart_watch.append(y)
    content = {
        'user':user,
        'analog':analog_watch,
        'digital':digital_watch,
        'smart':smart_watch,
        'filter':filter2,
        'total1': analog_total,
        'total2': digital_total,
        'total3': smart_total
    }
    return render(request, 'Aion/viewtransact.html', content)

def managerTransactionPageThree(request):
    user = get_object_or_404(User, pk = request.session['user'])
    transaction_list = Transaction.objects.all()
    product_list = Product.objects.all()
    product_list_bought = Product.objects.filter(product_bought = 1)
    product_no_transaction = Product.objects.filter(product_bought = 0)
    allName = {}
    totalPerProduct = {}
    a = 0
    for x in product_list:
        allName[a] = x
        totalPerProduct[a] = 0.0
        a = a + 1
    transaction_total = Transaction_Extension.objects.all()
    filter3 = 3
    content = {
        'user':user,
        'transaction':transaction_list,
        'filter': filter3,
        'totalPerProduct': transaction_total,
        'product': product_list_bought,
        'noTransactions': product_no_transaction
    }
    return render(request, 'Aion/viewtransact.html', content)

def transactionPage(request):
    user = get_object_or_404(User, pk = request.session['user'])
    user_transaction = Transaction.objects.filter(transaction_user = user)
    context ={
        'user': user,
        'transactions':user_transaction
    }
    return render(request, 'Aion/usertransactions.html', context)

def giveReviewPage(request, watchNo):
    user = get_object_or_404(User, pk = request.session['user'])
    chosen_watch = get_object_or_404(Product, pk=watchNo)
    context={
        'item': chosen_watch,
        'user': user
    }
    return render(request, 'Aion/reviewpage.html', context)

def finishReviewPage(request, watchNo):
    user = get_object_or_404(User, pk = request.session['user'])
    chosen_watch = get_object_or_404(Product, pk=watchNo)
    new_review = Product_Review(product_id=chosen_watch, product_user_review=user, product_comment=request.POST['UserReview'])
    new_review.save()
    good = 0
    watch_review = None
    transaction_list = Transaction.objects.all()
    try:
        watch_review = Product_Review.objects.filter(product_id=chosen_watch)
    except Product_Review.DoesNotExist:
        watch_review = None
    for x in transaction_list:
        if x.transaction_user == user:
            if x.product_id == chosen_watch:
                good = 1
    if watch_review:
        context = {
            'item':chosen_watch,
            'user':user,
            'good':good,
            'review': watch_review
        }
    else:
        context = {
        'item':chosen_watch,
        'good':good,
        'user':user
    }
    return render(request, 'Aion/watchdetails.html', context)

def transactionProcessed(request, watchNo):
    user = get_object_or_404(User, pk = request.session['user'])
    bought_watch = get_object_or_404(Product, pk=watchNo)
    bought_watch.product_quantity = bought_watch.product_quantity - int(request.POST['TransactionQuantity'])
    bought_watch.product_bought = 1
    bought_watch.save()
    costing = float(request.POST['TransactionQuantity']) * bought_watch.product_price
    make_transaction = Transaction(transaction_user=user, product_id=bought_watch, transaction_quantity=request.POST['TransactionQuantity'], transaction_order_total=costing)
    make_transaction.save()
    try:
        transactionExtension = Transaction_Extension.objects.get(product_id = bought_watch)
        transactionExtension.transaction_total = transactionExtension.transaction_total + costing
        transactionExtension.save()
    except Transaction_Extension.DoesNotExist:
        transactionExtension = Transaction_Extension(product_id=bought_watch, transaction_total=costing)
        transactionExtension.save()
    
    if user.user_privilege == '3':
        user_info = get_object_or_404(User_Info, user_id = user)
        context = {
            'user': user,
            'userInfo': user_info,
        }
    else:
        context = {
        'user': user,
	}
    return render(request, 'Aion/viewprofile.html', context)
    

def listManagersPage(request):
    user_list_product = User.objects.filter(user_privilege = '1')
    user_list_accounting = User.objects.filter(user_privilege = '2') 
    user = get_object_or_404(User, pk=request.session['user'])
    content = {
        'user':user,
        'productManagers': user_list_product,
        'accountingManagers': user_list_accounting,
    }
    return render(request, 'Aion/listofmanagers.html', content)

def loginPage(request):
    request.session['user'] = -1
    return render(request, 'Aion/login.html')

def signUpPage(request):
    request.session['user'] = -1
    form = EditProfileForm(request.POST , request.FILES)
    content = {
        'form':form
    }
    return render(request, 'Aion/signup.html', content)

def editWatchPage(request):
    user = get_object_or_404(User, pk=request.session['user'])
    watch_list = Product.objects.order_by('-id')
    content = {
        'user':user,
        'watchList':watch_list,
        
    }
    return render(request, 'Aion/listwatches.html', content)

def edittingWatchPage(request, watchNo):
    user = get_object_or_404(User, pk=request.session['user'])
    form = ProductImageForm(request.POST , request.FILES )
    watch = get_object_or_404(Product, pk=watchNo)
    content = {
        'user':user,
        'watch':watch,
        'form':form
    }
    return render(request, 'Aion/editwatch.html', content)

def addWatchPage(request):
    user = get_object_or_404(User, pk=request.session['user'])
    form = ProductImageForm(request.POST, request.FILES)
    content = {
        'user':user,
        'form':form
    }
    return render(request, 'Aion/addwatch.html', content)

def editProfilePage(request):
    form = EditProfileForm(request.POST, request.FILES)
    user = get_object_or_404(User, pk=request.session['user'])
    content = {
        'user': user,
        'form': form
    }
    return render(request, 'Aion/editprofile.html', content)

def addUserPage(request):
    user = get_object_or_404(User, pk=request.session['user'])
    admin_choices ={
        ('1', 'Product Manager'),
        ('2', 'Accounting Manager')
    }
    form = AdminUserImageForm(request.POST, request.FILES)
    form.fields['user_privilege'].choices = admin_choices
    content = {
        'user':user,
        'form':form
    }
    return render(request, 'Aion/adduser.html', content)

def adminAddUser(request):
    form = AdminUserImageForm(request.POST, request.FILES)
    user_list_product = User.objects.filter(user_privilege = '1')
    user_list_accounting = User.objects.filter(user_privilege = '2')
    user = get_object_or_404(User, pk=request.session['user'])
    if form.is_valid():
        user = form.save(commit=False)
        user.user_password = pbkdf2_sha256.encrypt(user.user_password, rounds=12000, salt_size=32)
        user.save()
        user_list_product = User.objects.filter(user_privilege = '1')
        user_list_accounting = User.objects.filter(user_privilege = '2')  
        user = get_object_or_404(User, pk=request.session['user'])
        context = {
            'productManagers': user_list_product,
            'accountingManagers': user_list_accounting,
            'user':user
        }
        return render(request, 'Aion/listofmanagers.html',context)
    else:
        context = {
            'productManagers': user_list_product,
            'accountingManagers': user_list_accounting,
            'user':user,
            'form':form
        }
        return render(request, 'Aion/adduser.html',context)
    

def accountingManagerFinancialDetails(request):
    transaction_list = Transaction.objects.all()
    context = {
        'transactionList': transaction_list
	}
    return render(request, 'Aion/<transaction results page>.html', context)

def productManagerWatchUpdate(request, watchNo):
    updating_watch = get_object_or_404(Product, pk=watchNo)
    form = ProductImageForm(request.POST, request.FILES, instance = updating_watch)
    watch_list = Product.objects.order_by('-id')
    user = get_object_or_404(User, pk=request.session['user'])
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        watch_list = Product.objects.order_by('-id')
        context = {
            'watchList': watch_list,
            'user':user
        }
        return render(request, 'Aion/listwatches.html',context)
    else:
        context = {
            'watchList': watch_list,
            'user':user
        }
        return render(request, 'Aion/listwatches.html',context)

def productManagerAddWatch(request):
    form = ProductImageForm(request.POST, request.FILES)
    watch_list = Product.objects.order_by('-id')
    user = get_object_or_404(User, pk=request.session['user'])
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        watch_list = Product.objects.order_by('-id')
        context = {
            'watchList': watch_list,
            'user':user
        }
        return render(request, 'Aion/listwatches.html',context)
    else:
        context = {
            'watchList': watch_list,
            'user':user
        }
        return render(request, 'Aion/listwatches.html',context)
    

def productManagerDeleteWatch(request, watchNo):
    delete_product = get_object_or_404(Product, pk=watchNo)
    delete_product.delete()
    watch_list = Product.objects.order_by('-id')
    user = get_object_or_404(User, pk=request.session['user'])
    context = {
        'watchList': watch_list,
        'user':user
	}
    return render(request, 'Aion/listwatches.html',context)

def homePage(request):

    user = get_object_or_404(User, pk = request.session['user'])
    watch_list = Product.objects.order_by('-id')
    context = {
		'watchList': watch_list,
        'user':user
	}
    return render(request, 'Aion/homepage.html',context)

def homeBase(request):
    # if 'session_key' in request.session:
    #     return HttpResponseRedirect('/Aion/homepage')

    watch_list = Product.objects.order_by('-id')
    context = {
		'watchList': watch_list,
	}

    if 'timeout' in request.session:
        context['timeout'] = True
        del request.session['timeout']
        user = get_object_or_404(User, pk=request.session['user'])
        logger.info("USER:{}-SESSION-TIMEDOUT".format(user.user_username))
    
    request.session.flush()

    if 'user' in request.session:
        if request.session['user'] > -1:
            user = get_object_or_404(User, pk=request.session['user'])
            logger.info("USER:{}-LOGOUT-SUCCESS".format(user.user_username))
    
    request.session['user'] = -1

    return render(request, 'Aion/homepage.html',context)


def watchDetail(request, watchNo):
    watch_detail = get_object_or_404(Product, pk=watchNo)
    watch_review = None
    transaction_list = Transaction.objects.all()
    good = 0
    try:
        watch_review = Product_Review.objects.filter(product_id=watch_detail)
    except Product_Review.DoesNotExist:
        watch_review = None
    if request.session['user'] > -1:
        user = get_object_or_404(User, pk=request.session['user'])
        for x in transaction_list:
            if x.transaction_user == user:
                if x.product_id == watch_detail:
                    good = 1
        if watch_review:
            context = {
                'item':watch_detail,
                'user':user,
                'good':good,
                'review': watch_review
            }
        else:
            context = {
            'item':watch_detail,
            'good':good,
            'user':user
        }
    else:
        if watch_review:
            context = {
                'item':watch_detail,
                'good':good,
                'review': watch_review
            }
        else:
            context = {
            'item':watch_detail,
            'good':good,
        }
    return render(request, 'Aion/watchdetails.html',context)

def watchListFilter(request, itemType):
    watch_list = Product.objects.filter(product_type = itemType)
    user = get_object_or_404(User, pk=request.session['user'])
    context = {
        'watchList': watch_list,
        'user':user
	}
    return render(request, 'Aion/homepage.html', context)
    
def signUp(request):
    userEditForm = EditProfileForm(request.POST, request.FILES)
    error = 0
    if userEditForm.is_valid():
        user_change = userEditForm.save(commit=False)
        user_change.user_username = userEditForm.cleaned_data['user_username']
        user_change.user_password = pbkdf2_sha256.encrypt(user_change.user_password, rounds=12000, salt_size=32)
        logger.info("ACCOUNT:{}-CREATION-SUCCESS".format(user_change.user_username))
        user_change.save()
    else:
        logger.info("ACCOUNT-CREATION-FAILED")

    user = User.objects.order_by('-id')[0]
    adding_user_info = User_Info(user_id = user, billing_house_number = request.POST['UserHouseNumber'], billing_street = request.POST['UserStreet'], billing_subdivision =request.POST['UserSubdivision'], billing_city =request.POST['UserCity'], billing_postal_code =request.POST['UserPostalCode'], billing_country =request.POST['UserCountry'], shipping_house_number =request.POST['UserSHouseNumber'], shipping_street =request.POST['UserSStreet'], shipping_subdivision =request.POST['UserSSubdivision'], shipping_city =request.POST['UserSCity'], shipping_postal_code =request.POST['UserSPostalCode'], shipping_country =request.POST['UserSCountry']) 
    adding_user_info.save()
    NewUser = User.objects.latest('id')
    adding_user_info = User_Info.objects.latest('id')
    password_ok = password_check(NewUser.user_username)
    if password_ok == 1:
        error = 0
        context = {
            'error':error,
        }
        return render(request, 'Aion/login.html', context)
    elif password_ok == 0:
        error = 1
        form = EditProfileForm(request.POST , request.FILES)
        context = {
            'error':error,
            'form':form
        }
        NewUser.delete()
        adding_user_info.delete()
        return render(request, 'Aion/signup.html', context)

def signIn(request):
    watch_list = Product.objects.order_by('-id')
    user_list = User.objects.all()
    request.session["user"] = -1
    error = 0
    user_list_product = User.objects.filter(user_privilege = '1')
    user_list_accounting = User.objects.filter(user_privilege = '2') 
    for x in user_list:
        if x.user_username == request.POST['SigningUserName']:
            if x.user_is_active:
                if x.verify_password(request.POST['SigningUserPassword']):
                    request.session["user"] = x.id

                    request.session['last_touch'] = datetime.now().isoformat()
                    logger.info("USER:{}-LOGIN-SUCCESS".format(x.user_username))
                else:
                    user = get_object_or_404(User, pk=x.id)
                    user.user_pass_tries += 1
                    user.save()
                    logger.info("USER:{}-LOGIN-FAILED".format(user.user_username))
                    if user.user_pass_tries == 5:
                        user.user_is_active = False
                        user.save()
                        logger.info("USER:{}-ACCOUNT-DISABLED".format(user.user_username))
                        
                        
            else:
                error = 1
                context = {
                    'error': error
                }
                logger.info("ACCESS-DENIED-DISABLED-ACCOUNT")
                return render(request, 'Aion/login.html', context)



    if request.session["user"] < 0:
        context = {
            'error': error
        }
        return render(request, 'Aion/login.html')
    user = get_object_or_404(User, pk=request.session['user'])
    if user.user_privilege == '0':
        form = AdminUserImageForm(request.POST, request.FILES)
        content = {
            'user':user,
            'productManagers': user_list_product,
            'accountingManagers': user_list_accounting,
        }
        return render(request, 'Aion/listofmanagers.html', content)
    if user.user_privilege == '1':
        content = {
            'watchList': watch_list,
            'user':user
        }
        return render(request, 'Aion/listwatches.html', content)
    if user.user_privilege == '2':
        transaction_list = Transaction.objects.all()
        filter1 = 1
        total = 0.0
        for x in transaction_list:
            total = total + x.transaction_order_total + 0.0
        content = {
            'user':user,
            'transaction':transaction_list,
            'filter': filter1,
            'total':total
        }
        return render(request, 'Aion/viewtransact.html', content)
    context = {
        'watchList': watch_list,
        'user':user
	}
    return render(request, 'Aion/homepage.html', context)

def buyWatch(request, watchNo):

    #---------------Credit card validation----------

    # number = 0
    # for digit in range(len(request.POST['creditcard']) - 1):
    #     if digit + 2 == len(request.POST['creditcard']):
    #         number += int(request.POST['creditcard'][digit + 1])

    #     if (digit + 1) % 2 == 0:
    #         number += int(request.POST['creditcard'][digit])
    #     else:
    #         if int(request.POST['creditcard'][digit]) * 2 > 9:
    #             split = int(request.POST['creditcard'][digit]) * 2
    #             split = str(split)
    #             number += int(split[:1]) + int(split[-1:])
    #         else:
    #             number += int(request.POST['creditcard'][digit]) * 2
    # if number % 10 != 0:
    #     creditcard not is_valid
    # else:
    #     creditcard valid

    #---------------Credit card validation----------

    user = get_object_or_404(User, pk = request.session['user'])
    bought_watch = get_object_or_404(Product, pk=watchNo)
    cost = float(request.POST['ProductQuantity'])
    costing = bought_watch.product_price * cost
    context = {
        'user':user, 
        'item':bought_watch,
        'cost': costing, 
        'quantity': request.POST['ProductQuantity']
    }
    return render(request, 'Aion/shoppingcart.html', context)

def myProfile(request):
    user = get_object_or_404(User, pk = request.session['user'])
    if user.user_privilege == '3':
        user_info = get_object_or_404(User_Info, user_id = user)
        context = {
            'user': user,
            'userInfo': user_info,
        }
    else:
        context = {
        'user': user,
	}
    return render(request, 'Aion/viewprofile.html', context)

def profileUpdate(request):
    user = get_object_or_404(User, pk=request.session['user'])
    userEditForm = EditProfileForm(request.POST, request.FILES, instance = user)
    if userEditForm.is_valid():
        user_change = userEditForm.save(commit=False)
        user_change.save()
        user = get_object_or_404(User, pk=request.session['user'])
        
    if user.user_privilege == '3':
        updating_user_info = get_object_or_404(User_Info, user_id = user)
        updating_user_info.billing_house_number = request.POST['UpdatingBillHouse']
        updating_user_info.billing_street = request.POST['UpdatingBillStreet']
        updating_user_info.billing_subdivision = request.POST['UpdatingBillSubdivision']
        updating_user_info.billing_city = request.POST['UpdatingBillCity']
        updating_user_info.billing_postal_code = request.POST['UpdatingBillPostal']
        updating_user_info.billing_country = request.POST['UpdatingBillCountry']
        updating_user_info.shipping_house_number = request.POST['UpdatingShipHouse']
        updating_user_info.shipping_street = request.POST['UpdatingShipStreet']
        updating_user_info.shipping_subdivision = request.POST['UpdatingShipSubdivision']
        updating_user_info.shipping_city = request.POST['UpdatingShipCity']
        updating_user_info.shipping_postal_code = request.POST['UpdatingShipPostal']
        updating_user_info.shipping_country = request.POST['UpdatingShipCountry']
        updating_user_info.save()
        user_info = get_object_or_404(User_Info, user_id = user)
        context = {
            'user': user, 
            'userInfo': user_info,
        }
    else:
        context = {
            'user': user
        }
    return render(request, 'Aion/viewprofile.html', context)