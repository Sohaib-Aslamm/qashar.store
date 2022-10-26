from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from adminpannel.models import contact_us, amazonProduct, WhatPeopleSay
# Create your views here.


def Home(request):
    PRDCTS = amazonProduct.objects.filter(featured='Featured').order_by('-sNo')
    paginator = Paginator(PRDCTS, 20)
    pageNo = request.GET.get('page')
    PRDCTSFINAL = paginator.get_page(pageNo)
    totalPages = PRDCTSFINAL.paginator.num_pages
    PRDCTGRY = amazonProduct.objects.filter(featured='Featured').values('category').distinct()
    testimonials = WhatPeopleSay.objects.all();
    context = {'PRDCTS': PRDCTSFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'PRDCTGRY': PRDCTGRY, 'testimonials': testimonials}
    return render(request, 'home.html', context)


def Products(request):
    PRDCTS1 = amazonProduct.objects.order_by('-sNo')
    paginator = Paginator(PRDCTS1, 50)
    pageNo = request.GET.get('page')
    PRDCTSFINAL1 = paginator.get_page(pageNo)
    totalPages = PRDCTSFINAL1.paginator.num_pages
    PRDCTGRY = amazonProduct.objects.values('category').distinct()
    context = {'PRDCTS': PRDCTSFINAL1, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'PRDCTGRY': PRDCTGRY}
    return render(request, 'products.html', context)


def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        sv = contact_us(name=name, subject=subject, email=email, phone=phone, message=message)
        sv.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('/Contact')
    return render(request, 'contact.html')


def DetailRecord(request, id, type):
    if type == 'productDetail':
        Record = amazonProduct.objects.get(sNo=id)
        context = {'rec': Record }
        return render(request, 'product_detail.html', context)




def About(request):
    return render(request, 'about.html')


def Services(request):
    return render(request, 'services.html')

