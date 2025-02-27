from django import forms 
from django.contrib.auth.models import User
from  First_app.models import Userinfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')

class UserinfoForm(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields=('F_ID','profile_P')
