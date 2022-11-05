# Create your models here.
import django.utils.timezone
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

category = (
    ('Cosmetics', 'Cosmetics'),
    ('Wears', 'Wears'),
    ('Electronics', 'Electronics'),
    ('Computer', 'Computer'),
    ('Decoration', 'Decoration'),
    ('Wireless', 'Wireless'),

)


yesNo = (
    ('YES', 'YES'),
    ('NO', 'NO'),

)

Featured = (
    ('Not_Featured', 'Not_Featured'),
    ('Featured', 'Featured'),

)

inStock = (
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
)


ServiceType = (
    ('RegularService', 'RegularService'),
    ('MainService', 'MainService'),
)


class amazonProduct(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    cPrice = models.CharField(max_length=100, default="")
    dPrice = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=category, default="")
    brand = models.CharField(max_length=100, default="")
    color = models.CharField(max_length=100, default="")
    availability = models.CharField(max_length=100, choices=inStock, default="")
    featured = models.CharField(max_length=100, choices=Featured, default="")
    heading1 = models.CharField(max_length=255, default="")
    heading2 = models.CharField(max_length=255, default="")
    heading3 = models.CharField(max_length=255, default="")
    heading4 = models.CharField(max_length=255, default="")
    answer1 = models.CharField(max_length=255, default="")
    answer2 = models.CharField(max_length=255, default="")
    answer3 = models.CharField(max_length=255, default="")
    answer4 = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    buyLink = models.CharField(max_length=255, default="")
    mainIcon = models.FileField(upload_to='AmazonProducts/MainIcon', default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())


class WhatPeopleSay(models.Model):
    name = models.CharField(max_length=200, default="")
    designation = models.CharField(max_length=200, default="")
    say_something = models.TextField(default="")
    icon = models.ImageField(upload_to='Home/Testimonials', default="")


class contact_us(models.Model):
    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")


class SocialMedia(models.Model):
    sNo = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, default="")
    skype = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    github = models.CharField(max_length=100, default="")
    linkedin = models.CharField(max_length=100, default="")
    google_plus = models.CharField(max_length=100, default="")
    youtube = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=100, default="")


class userBlog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    heading = models.CharField(max_length=255, default="")
    tags = models.CharField(max_length=255, default="")
    quote = models.CharField(max_length=255, default="")
    quote_by = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    Icon = models.ImageField(upload_to='Blog/Icons', default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())


class blog_Review(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")
    post = models.ForeignKey(userBlog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)

