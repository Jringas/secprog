"""dotExe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .import views
app_name = 'Aion'

urlpatterns = [
    url(r'adminAddUser$' ,views.adminAddUser ,name='adminAddUser'),
    url(r'accountingManagerFinancialDetails$' ,views.accountingManagerFinancialDetails ,name='accountingManagerFinancialDetails'),
    url(r'productManagerWatchUpdate/(?P<watchNo>[0-9]+)$' ,views.productManagerWatchUpdate ,name='productManagerWatchUpdate'),
    url(r'productManagerAddWatch$' ,views.productManagerAddWatch ,name='productManagerAddWatch'),
    url(r'productManagerDeleteWatch/(?P<watchNo>[0-9]+)$' ,views.productManagerDeleteWatch ,name='productManagerDeleteWatch'),
    url(r'homePage$',views.homePage ,name='homePage'),
    url(r'watchDetail/(?P<watchNo>[0-9]+)$' ,views.watchDetail ,name='watchDetail'),
    url(r'watchListFilter$' ,views.watchListFilter ,name='watchListFilter'),
    url(r'signUp$' ,views.signUp ,name='signUp'),
    url(r'signIn$' ,views.signIn ,name='signIn'),
    url(r'buyWatch/(?P<watchNo>[0-9]+)$' ,views.buyWatch ,name='buyWatch'),
    url(r'myProfile$' ,views.myProfile ,name='myProfile'),
    url(r'profileUpdate$' ,views.profileUpdate ,name='profileUpdate'),
    url(r'loginPage$' ,views.loginPage ,name='loginPage'),
    url(r'signUpPage$' ,views.signUpPage ,name='signUpPage'),
    url(r'editProfilePage$' ,views.editProfilePage ,name='editProfilePage'),
    url(r'addWatchPage$' ,views.addWatchPage ,name='addWatchPage'),
    url(r'editWatchPage$' ,views.editWatchPage ,name='editWatchPage'),
    url(r'edittingWatchPage/(?P<watchNo>[0-9]+)$' ,views.edittingWatchPage ,name='edittingWatchPage'),
    url(r'addUserPage$' ,views.addUserPage ,name='addUserPage'),
    url(r'listManagersPage$' ,views.listManagersPage ,name='listManagersPage'),
    url(r'transactionProcessed/(?P<watchNo>[0-9]+)$' ,views.transactionProcessed ,name='transactionProcessed'),
    url(r'giveReviewPage/(?P<watchNo>[0-9]+)$' ,views.giveReviewPage ,name='giveReviewPage'),
    url(r'finishReviewPage/(?P<watchNo>[0-9]+)$' ,views.finishReviewPage ,name='finishReviewPage'),
    url(r'addUserPage$' ,views.addUserPage ,name='addUserPage'),
    url(r'transactionPage$' ,views.transactionPage ,name='transactionPage'),
    url(r'managerTransactionPageOne$' ,views.managerTransactionPageOne ,name='managerTransactionPageOne'),
    url(r'managerTransactionPageTwo$' ,views.managerTransactionPageTwo ,name='managerTransactionPageTwo'),
    url(r'managerTransactionPageThree$' ,views.managerTransactionPageThree ,name='managerTransactionPageThree'),
    url(r'^$',views.homeBase ,name='homeBase'),
]
