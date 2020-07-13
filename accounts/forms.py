from django import forms
from django.contrib.auth import authenticate
from accounts.models import Account



class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = Account
        fields = ['username','email','password','confirm_password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password' : forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'confirm_password' : forms.PasswordInput(attrs={'placeholder': 'confirm_password'}),
    }
        



class UserForm(forms.ModelForm):

    class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
