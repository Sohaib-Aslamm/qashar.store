from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from adminpannel.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login as auth_login, logout
from adminpannel.forms import UserForm, amazonProductsForm, WhatPeopleSForm
from adminpannel.models import amazonProduct, contact_us, WhatPeopleSay, userBlog


# Create your views here

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Auth Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        URFM = UserForm(request.POST, request.FILES)
        if URFM.is_valid():
            URFM.save()
            user = URFM.cleaned_data.get('username')
            messages.success(request, f'Hey !  {user} your account created successfully')
            return redirect('/user_login')
    else:
        URFM = UserForm()
    return render(request, 'User_Register.html', {'form': URFM})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f'Welcome to your portfolio {user}')
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')



def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out !')
    return redirect('/user_login')



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Insert Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



@login_required(login_url='/user_login')
# @allowed_users(allowed_roles=[])
def adminHome(request):
    my_messages = contact_us.objects.all()
    return render(request, 'HomeAdmin.html', {'my_messages': my_messages})


@login_required(login_url='/user_login')
def viewMessage(request, id):
    messages_detail = contact_us.objects.get(id=id)
    return render(request, 'viewMessages.html', {'messages_detail': messages_detail})




@login_required(login_url='/user_login')
def adminAmazonProducts(request):
    if request.method == 'POST':
        PRDTFM = amazonProductsForm(request.POST, request.FILES)
        if PRDTFM.is_valid():
            TIT = PRDTFM.cleaned_data['title']
            CPR = PRDTFM.cleaned_data['cPrice']
            DPR = PRDTFM.cleaned_data['dPrice']
            AVLBTY = PRDTFM.cleaned_data['availability']
            BRND = PRDTFM.cleaned_data['brand']
            CLR = PRDTFM.cleaned_data['color']
            CTGRY = PRDTFM.cleaned_data['category']
            FTRD = PRDTFM.cleaned_data['featured']
            HD1 = PRDTFM.cleaned_data['heading1']
            ANS1 = PRDTFM.cleaned_data['answer1']
            HD2 = PRDTFM.cleaned_data['heading2']
            ANS2 = PRDTFM.cleaned_data['answer2']
            HD3 = PRDTFM.cleaned_data['heading3']
            ANS3 = PRDTFM.cleaned_data['answer3']
            HD4 = PRDTFM.cleaned_data['heading4']
            ANS4 = PRDTFM.cleaned_data['answer4']
            BLINK = PRDTFM.cleaned_data['buyLink']
            DESC = PRDTFM.cleaned_data['description']
            ICON = PRDTFM.cleaned_data['mainIcon']
            CRA = PRDTFM.cleaned_data['created_at']
            reg = amazonProduct(title=TIT, cPrice=CPR, dPrice=DPR, availability=AVLBTY, brand=BRND, color=CLR,
                                category=CTGRY, featured=FTRD, created_at=CRA,
                                heading1=HD1, heading2=HD2, heading3=HD3, heading4=HD4, answer1=ANS1, answer2=ANS2,
                                answer3=ANS3, answer4=ANS4, buyLink=BLINK, description=DESC, mainIcon=ICON)
            reg.save()
            PRDTFM = amazonProductsForm()
    else:
        PRDTFM = amazonProductsForm()

    PRDTDT = amazonProduct.objects.all().order_by('-sNo')
    paginator = Paginator(PRDTDT, 10)
    pageNo = request.GET.get('page')
    PRDTDTFINAL = paginator.get_page(pageNo)
    totalPages = PRDTDTFINAL.paginator.num_pages
    context = {'PRDTDT': PRDTDTFINAL, 'form': PRDTFM, 'lastPage': totalPages, 'pageList': [n+1 for n in range(totalPages)]}
    return render(request, 'amazonProduct.html', context)




@login_required(login_url='/user_login')
def adminPeopleSay(request):
    if request.method == 'POST':
        WPSFM = WhatPeopleSForm(request.POST, request.FILES)
        if WPSFM.is_valid():
            NM = WPSFM.cleaned_data['name']
            DESG = WPSFM.cleaned_data['designation']
            SAY = WPSFM.cleaned_data['say_something']
            ICN = WPSFM.cleaned_data['icon']
            reg = WhatPeopleSay(name=NM, designation=DESG, say_something=SAY, icon=ICN)
            reg.save()
            WPSFM = WhatPeopleSForm()
    else:
        WPSFM = WhatPeopleSForm()
    WPSDT = WhatPeopleSay.objects.all()
    return render(request, 'adminPeopleSay.html', {'form': WPSFM, 'WPSDT': WPSDT})



@login_required(login_url='/user_login')
def adminblog(request):
    if request.method == 'POST':
        TIT = request.POST.get('title')
        HD = request.POST.get('heading')
        TGS = request.POST.get('tags')
        QT = request.POST.get('quote')
        QTBY = request.POST.get('quote_by')
        CRA = request.POST.get('created_at')
        DSC = request.POST.get('editor1')
        ICN = request.FILES['icon']
        reg = userBlog(title=TIT, heading=HD, tags=TGS, quote=QT, quote_by=QTBY, description=DSC, Icon=ICN,
                       created_at=CRA)
        reg.save()

    BLGdata = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLGdata, 10)
    pageNo = request.GET.get('page')
    BLGdataFINAL = paginator.get_page(pageNo)
    totalPages = BLGdataFINAL.paginator.num_pages
    context = {'BLGdata': BLGdataFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)]}
    return render(request, 'adminBlog.html', context)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Delete Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



@login_required(login_url='/user_login')
def MasterDelete(request, type):
    if type == 'Message':
        MasterDeleter = contact_us.objects.all()
        MasterDeleter.delete()
        return redirect('/admin')


@login_required(login_url='/user_login')
def Delete(request, id, type):
    if type == 'amazonProducts':
        DeleteRecord = amazonProduct.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/adminAmazonProducts')

    if type == 'PeopleSay':
        DeleteRecord = WhatPeopleSay.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminPeopleSay')

    if type == 'blog':
        DeleteRecord = userBlog.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/adminblog')


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Update Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
def Update(request, id, type):
    if type == 'amazonProducts':
        if request.method == 'POST':
            UpdateRecord = amazonProduct.objects.get(sNo=id)
            UpdateForm = amazonProductsForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminAmazonProducts')
        else:
            UpdateRecord = amazonProduct.objects.get(sNo=id)
            UpdateForm = amazonProductsForm(instance=UpdateRecord)
        return render(request, 'Update/updateAmazonProduct.html', {'form': UpdateForm})

    if type == 'PeopleSay':
            if request.method == 'POST':
                UpdateRecord = WhatPeopleSay.objects.get(id=id)
                UpdateForm = WhatPeopleSForm(request.POST, request.FILES, instance=UpdateRecord)
                if UpdateForm.is_valid():
                    UpdateForm.save()
                    return redirect('/adminPeopleSay')
            else:
                UpdateRecord = WhatPeopleSay.objects.get(id=id)
                UpdateForm = WhatPeopleSForm(instance=UpdateRecord)
            return render(request, 'Update/updatePeopleSay.html', {'form': UpdateForm})

    if type == 'blog':
        UpdateForm = userBlog.objects.get(sNo=id)
        if request.method == 'POST':
            UpdateForm.title = request.POST.get('title')
            UpdateForm.heading = request.POST.get('heading')
            UpdateForm.tags = request.POST.get('tags')
            UpdateForm.quote = request.POST.get('quote')
            UpdateForm.quote_by = request.POST.get('quote_by')
            UpdateForm.description = request.POST.get('editor1')
            UpdateForm.save()
            return redirect('/adminblog')

        return render(request, 'Update/updateBlog.html', {'form': UpdateForm})