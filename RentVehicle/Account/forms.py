from django.contrib.auth import get_user_model#User model currently active in the project
from django.contrib.auth.forms import UserCreationForm#for sign up page
from . import models
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'#The label you want to display on the form
        self.fields['email'].label = 'Email Address'

class RenterForm(forms.ModelForm):
    class Meta:
        model = models.Renter
        exclude = ['user']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        exclude = ['user']
