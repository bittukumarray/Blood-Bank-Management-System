from django.shortcuts import render
from .models import UserAddress, UserProfile
from . import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'home/index.html')


def SignUp(request):

    userform=forms.UserForm()
    useraddressform=forms.UserAddressForm()

    if request.method=="POST":
        userform=forms.UserForm(data = request.POST)
        useraddressform=forms.UserAddressForm(data = request.POST)
        birth = request.POST['birth']

        if userform.is_valid() and useraddressform.is_valid():
            user=userform.save(commit=False)
            useraddress=useraddressform.save(commit=False)
            user.set_password(user.password)
            user.save()
            useraddress.user=user
            useraddress.birth=birth
            useraddress.save()

            UserProfile.objects.create(user = user)


            return HttpResponseRedirect(reverse("home:index"))
        else:
            return HttpResponse("invalid data")

    return render(request,'home/signup.html',{'form':userform,'address':useraddressform})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))



def LogIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)



                return HttpResponseRedirect(reverse("home:index"))

        else:
            return HttpResponse("<h2>username or password are incorrect</h2>")


    else:
        return render(request,'home/login.html',)


    return render(request,'home/login.html',)


def about(request):
    return render(request,'home/base.html',)
