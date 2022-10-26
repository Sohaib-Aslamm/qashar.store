from django.urls import path
from Home import views

urlpatterns = [

    path('', views.Home, name="Home"),
    path('home', views.Home, name="home"),
    path('About', views.About, name="About"),
    path('Products', views.Products, name="Products"),
    path('Services', views.Services, name="Services"),
    path('Contact', views.Contact, name="Contact"),
    path('DetailRecord/<int:id>/<str:type>', views.DetailRecord, name="DetailRecord")

]