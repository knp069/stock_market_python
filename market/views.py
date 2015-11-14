from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.db.models import Q
from django.http import *
from models import *
from tasks import *

# Create your views here.

def userSignup(request):

    registered=False
    Context={'c': None , 'c':None}
    if request.POST:
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        existing_user = User.objects.filter(Q(username=username)|Q(email=email)).count()
        if existing_user==0:
            temp_user = User()

            temp_user.username = username
            temp_user.email = email
            temp_user.set_password(password)
            temp_user.save()
            existing_user1 = User.objects.filter(Q(username=username)|Q(email=email)).count()
            if existing_user1!=0:
                tmp_stock_holder = stock_holder()
                tmp_stock_holder.user = temp_user

                if gender == 'male':
                    tmp_stock_holder.gender = 1
                else :
                    tmp_stock_holder.gender = 0

                tmp_stock_holder.phone = phone
                tmp_stock_holder.save()
                c=1
                message="registration successfull"
                Context['c']=c
                Context['error_msg']=message
                return render(request,'market/signup.html',Context)
            else:
                c=1
                message='error in registration'
                Context['c']=c
                Context['error_msg']=message
                return render(request,'market/signup.html',Context)
        else:
            c=1
            message='user already registered'
            Context['c']=c
            Context['error_msg']=message
            return render(request,'market/signup.html',Context)


    else:
        return render(request,'market/signup.html',Context)


def brokerSignup(request):
    registered=False
    Context={'c': None , 'c':None}
    if request.POST:
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        existing_user = User.objects.filter(Q(username=username)|Q(email=email)).count()
        if existing_user==0:
            temp_user = User()

            temp_user.username = username
            temp_user.email = email
            temp_user.set_password(password)
            temp_user.save()
            existing_user1 = User.objects.filter(Q(username=username)|Q(email=email)).count()
            if existing_user1!=0:
                tmp_broker = broker()
                tmp_broker.user = temp_user

                if gender == 'male':
                    tmp_broker.gender = 1
                else :
                    tmp_broker.gender = 0

                tmp_broker.phone_number = phone
                tmp_broker.save()
                c=1
                message="registration successfull"
                Context['c']=c
                Context['error_msg']=message
                return render(request,'market/broker-signup.html',Context)
            else:
                c=1
                message='error in registration'
                Context['c']=c
                Context['error_msg']=message
                return render(request,'market/broker-signup.html',Context)
        else:
            c=1
            message='user already registered'
            Context['c']=c
            Context['error_msg']=message
            return render(request,'market/broker-signup.html',Context)


    else:
        return render(request,'market/broker-signup.html',Context)

def ownerSignup(request):
    registered=False
    Context={'c': None , 'c':None}
    if request.POST:
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company')

        existing_user = User.objects.filter(Q(username=username)|Q(email=email)).count()
        if existing_user==0:
            temp_user = User()

            temp_user.username = username
            temp_user.email = email
            temp_user.set_password(password)
            temp_user.save()
            existing_user1 = User.objects.filter(Q(username=username)|Q(email=email)).count()
            if existing_user1!=0:
                tmp_owner = owner()
                tmp_owner.user = temp_user

                if gender == 'male':
                    tmp_owner.gender = 1
                else :
                    tmp_owner.gender = 0

                tmp_owner.phone_number = phone
                tmp_company = company()
                tmp_company.name = company_name
                tmp_company.save()
                tmp_owner.company = tmp_company
                tmp_owner.save()
                c=1
                message="registration successfull"
                Context['c']=c
                Context['error_msg']=message
                return render(request,'market/owner-signup.html',Context)
            else:
                c=1
                message='error in registration'
                Context['c']=c
                Context['error_msg']=message
                return render(request,'market/owner-signup.html',Context)
        else:
            c=1
            message='user already registered'
            Context['c']=c
            Context['error_msg']=message
            return render(request,'market/owner-signup.html',Context)


    else:
        return render(request,'market/owner-signup.html',Context)

def userlogin(request):
    if request.POST:
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password);
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/stocks/stockholder-panel')
            else:
                return HttpResponse('<h1>user not active</h1>')
        else:
            return HttpResponse('<h1>user credentials are wrong</h1>')
    else:
        return render(request,'market/login.html')

def ownerLogin(request):
    return render(request,'market/owner-login.html')

def brokerLogin(request):
    if request.POST:
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password);
        if user is not None:
            if broker.objects.get(user=user) is not None:
                login(request,user)
                return HttpResponseRedirect('/stocks/broker-panel/')
            else:
                return HttpResponse('<h1>user not active</h1>')
        else:
            return HttpResponse('<h1>user credentials are wrong</h1>')
    else:
        return render(request,'market/broker-login.html')

def index(request):
    if request.user:
        if type(request.user) == stock_holder:
            return HttpResponseRedirect('/stocks/stockholder-panel/')

    company_list = []
    company_list = company.objects.all()
    context = {'company_list':company_list}
    return render(request,'market/index.html',context)

@login_required()
def brokerPanel(request):
    company_list = []
    company_list = company.objects.all()
    context = {'company_list':company_list}
    return render(request,'market/brokerpanel.html',context)

@login_required()
def stockHolderPanel(request):
    user = request.user
    stock_holder_user = stock_holder.objects.filter(user=user)[0]
    stock_owner=[]
    stock_owner = stockowner.objects.filter(owner=stock_holder_user)
    context={}
    context['stocks']=stock_owner
    return render(request,'market/stockholderpanel.html',context)


@login_required()
def userprofile(request):
    user=request.user
    stock_user =  stock_holder.objects.filter(user=user)[0]
    context ={'user':stock_user}
    return render(request , 'market/userprofile.html',context)

def logout_users(request):
    logout(request)
    return HttpResponseRedirect('/stocks/')


def makeTransaction(request):
    buyorsell = request.POST.get('buyorsell');
    username = request.POST.get('uname')
    password = request.POST.get('password')
    company_name = request.POST.get('company')
    numberOfShare = int(request.POST.get('num'))
    costOfShare = float(company.objects.filter(name=company_name)[0].price)
    stock_company = company.objects.filter(name=company_name)[0]
    user = authenticate(username=username,password=password)
    usern = stock_holder.objects.filter(user=user)[0]
    user=usern
    if user is not None:
        availableAmount = float(user.hard_asset)
        if buyorsell == 'buy':
            if availableAmount >= numberOfShare*costOfShare:
                if len(stockowner.objects.filter(owner=user,stock_owned=stock_company)) == 0:
                    tmpstockowner = stockowner()
                    tmpstockowner.owner = user
                    tmpstockowner.stock_owned = stock_company
                    tmpstockowner.number_of_stock = numberOfShare
                    tmpstockowner.save()
                    user.hard_asset -= numberOfShare*costOfShare
                    user.save()
                    stock_company.available_stock -=numberOfShare
                    stock_company.save()
                    return HttpResponseRedirect('/stocks/broker-panel/')
                else:
                    tmpstockowner = stockowner.objects.filter(owner=user,stock_owned=stock_company)[0]
                    tmpstockowner.number_of_stock += numberOfShare
                    tmpstockowner.save()
                    return HttpResponseRedirect('/stocks/broker-panel/')
        else:
            if len(stockowner.objects.filter(owner=user,stock_owned=stock_company)) == 0:
                return HttpResponseRedirect('/stocks/broker-panel/')
            else:
                tmpstockowner = stockowner.objects.filter(owner=user,stock_owned=stock_company)[0]
                tmpstockowner.number_of_stock -= numberOfShare
                user.hard_asset += numberOfShare*costOfShare
                user.save()
                stock_company.available_stock +=numberOfShare
                stock_company.save()
                tmpstockowner.save()
                return HttpResponseRedirect('/stocks/broker-panel/')
            return HttpResponseRedirect('/stocks/broker-panel/')
    else:
        return HttpResponseRedirect('/stocks/broker-panel/')




