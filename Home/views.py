from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from adminpannel.models import contact_us, Q_Products, amazonProduct, WhatPeopleSay,  userBlog, blog_Review, \
    SocialMedia, Place_Order
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.


def Home(request):
    PRDCTS = Q_Products.objects.filter(featured='Featured').order_by('-id')
    paginator = Paginator(PRDCTS, 20)
    pageNo = request.GET.get('page')
    PRDCTSFINAL = paginator.get_page(pageNo)
    totalPages = PRDCTSFINAL.paginator.num_pages
    PRDCTGRY = Q_Products.objects.filter(featured='Featured').values('category').distinct()
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

def blogHome(request):
    BLOGDATA = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLOGDATA, 9)
    pageNo = request.GET.get('page')
    BLOGDATAFINAL = paginator.get_page(pageNo)
    totalPages = BLOGDATAFINAL.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'blog.html', context)


def blogReview(request):
    if request.method == 'POST':
        postSno = request.POST.get('postSno')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = userBlog.objects.get(sNo=postSno)
        sv = blog_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()

        return redirect('/blog')


def DetailRecord(request, id, type):
    if type == 'productDetail':
        Record = Q_Products.objects.get(id=id)
        context = {'rec': Record}
        return render(request, 'product_detail.html', context)

    if type == 'amazonProductDetail':
        Record = amazonProduct.objects.get(sNo=id)
        context = {'rec': Record}
        return render(request, 'amazonProductDetail.html', context)

    if type == 'blogDetail':
        rdPost = userBlog.objects.filter(sNo=id)
        coments = blog_Review.objects.filter(post__in=rdPost).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'rdPost': rdPost, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments}
        return render(request, 'read_post.html', context)

    if type == 'track_order':
        Record = Place_Order.objects.get(id=id)
        p_id = Record.product_id.replace("[", "").replace("]", "").replace("'", "")
        p_id = p_id.split(",")
        product_data = Q_Products.objects.filter(id__in=p_id).values('name', 'image')
        price_total = Record.p_total.replace("[", "").replace("]", "").replace("'", "")
        p_quantity = Record.p_quantity.replace("[", "").replace("]", "").replace("'", "")
        p_price = Record.p_price.replace("[", "").replace("]", "").replace("'", "")

        price_total = price_total.split(",")
        p_quantity = p_quantity.split(",")
        p_price = p_price.split(",")

        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data}
        return render(request, 'track_order_detail.html', context)

    if type == 'order':
        Record = Place_Order.objects.get(id=id)
        p_id = Record.product_id.replace("[", "").replace("]", "").replace("'", "")
        p_id = p_id.split(",")
        product_data = Q_Products.objects.filter(id__in=p_id).values('name', 'image')
        price_total = Record.p_total.replace("[", "").replace("]", "").replace("'", "")
        p_quantity = Record.p_quantity.replace("[", "").replace("]", "").replace("'", "")
        p_price = Record.p_price.replace("[", "").replace("]", "").replace("'", "")
        price_total = price_total.split(",")
        p_quantity = p_quantity.split(",")
        p_price = p_price.split(",")
        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data}
        if request.method == 'POST':
            Record.status = request.POST.get('status')
            Record.save()
            return redirect('/orders')

        return render(request, 'order_detail.html', context)


def About(request):
    return render(request, 'about.html')


def Services(request):
    return render(request, 'services.html')


# <------------------------------------------ Cart System ------------------------------------>


@login_required(login_url='/user_login')
def cart_add(request, id):
    cart = Cart(request)
    product = Q_Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("/home")


@login_required(login_url='/user_login')
def item_clear(request, id):
    cart = Cart(request)
    product = Q_Products.objects.get(id=id)
    cart.remove(product)
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def item_increment(request, id):
    cart = Cart(request)
    product = Q_Products.objects.get(id=id)
    cart.add(product=product)
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def item_decrement(request, id):
    cart = Cart(request)
    product = Q_Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def cart_detail(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'SMDT': SMDT, 'RCPST': RCPST, }
    return render(request, 'cart_detail.html', context)


@login_required(login_url='/user_login')
def checkout(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'SMDT': SMDT, 'RCPST': RCPST, }
    return render(request, 'checkout.html', context)


@login_required(login_url='/user_login')
def place_order(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        status = request.POST.get('status')
        product_id = request.POST.getlist('product_id')
        p_price = request.POST.getlist('p_price')
        p_quantity = request.POST.getlist('p_quantity')
        p_total = request.POST.getlist('p_total')
        p_grand_total = request.POST.get('p_grand_total')
        c_name = request.POST.get('c_name')
        c_email = request.POST.get('c_email')
        c_phone = request.POST.get('c_phone')
        c_city = request.POST.get('c_city')
        c_zip = request.POST.get('c_zip')
        c_country = request.POST.get('c_country')
        c_address1 = request.POST.get('c_address1')
        c_address2 = request.POST.get('c_address2')
        reg = Place_Order(product_id=product_id, user_id=user_id, status=status, p_price=p_price, p_quantity=p_quantity,
                          p_total=p_total, p_grand_total=p_grand_total, c_name=c_name, c_email=c_email, c_phone=c_phone,
                          c_city=c_city, c_zip=c_zip, c_country=c_country, c_address1=c_address1, c_address2=c_address2)
        reg.save()
        cart = Cart(request)
        cart.clear()
        return redirect('/order_placed')
    return render(request, 'checkout.html')


def trackOrder(request):
    u_id = request.user.id
    product_orders = Place_Order.objects.filter(user_id=u_id).order_by('-id')[:8]
    context = {'product_orders': product_orders}
    return render(request, 'track_order.html', context)


def orderDone(request):
    return render(request, 'Order_Done.html')

# <------------------------------------------ Detail Of Records ------------------------------------>