from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from adminpannel.models import amazonProduct, WhatPeopleSay, Q_Products


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter user name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'choose password'}),
            'password2': forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'confirm password'}),
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Q_Products
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'cPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'current price'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'discounted price'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter brand'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'featured': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blue, Red, Black'}),
            'label1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'input1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }


class amazonProductsForm(forms.ModelForm):
    class Meta:
        model = amazonProduct
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'cPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'current price'}),
            'dPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'discounted price'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter brand name'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blue, Red, Black'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'featured': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'buyLink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter buying link'}),
            'heading1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Item weight'}),
            'heading2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Size'}),
            'heading3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Label'}),
            'heading4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Label'}),
            'answer1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '7.8 Ounces'}),
            'answer2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jumbo, Double'}),
            'answer3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'answer4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }




class WhatPeopleSForm(forms.ModelForm):
    class Meta:
        model = WhatPeopleSay
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your designation'}),
            'say_something': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Say Something'}),
        }


