from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        #print("yes")
        if password != confirm_password:
            #print("no")
            #return HttpResponse("password and confirm password didn't match")
            raise forms.ValidationError("password and confirm password didn't match")


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        exclude = ['user','birth']

class Upload_Image(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image','status']



class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class UploadAddress(forms.ModelForm):
    class Meta:
        model = UserAddress
        exclude = ['user','blood','gender']


