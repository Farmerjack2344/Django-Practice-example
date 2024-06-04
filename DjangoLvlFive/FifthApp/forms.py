from django import forms
from django.contrib.auth.models import User
from FifthApp.models import UserProfileInfo

# Always put form after otherwise the framework will get confused
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username', 'email', 'password')# Could ad fist and last name if you want to


class UserProfileInfoForm(forms.ModelForm):


    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
