from django.urls import path
from Home import views

urlpatterns = [

    path('', views.Home, name="Home"),
    path('home', views.Home, name="home"),
    path('About', views.About, name="About"),
    path('Products', views.Products, name="Products"),
    path('Services', views.Services, name="Services"),
    path('Contact', views.Contact, name="Contact"),
    path('blog', views.blogHome, name="blog"),
    path('addReview', views.blogReview, name="addReview"),
    path('DetailRecord/<int:id>/<str:type>', views.DetailRecord, name="DetailRecord"),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cartDetail', views.cart_detail, name='cartDetail'),
    path('checkout', views.checkout, name='checkout'),
    path('placeOrder', views.place_order, name='placeOrder'),
    path('order_placed', views.orderDone, name="order_placed"),
    path('track_order', views.trackOrder, name='track_order'),

]