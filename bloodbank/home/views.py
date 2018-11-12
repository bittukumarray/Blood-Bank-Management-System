from django.shortcuts import render
from .models import UserAddress, UserProfile, Wallet, UserHistory
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
            Wallet.objects.create(user = user)
            UserHistory.objects.create(user = user)


            return HttpResponseRedirect(reverse("home:index"))

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
            return HttpResponseRedirect(reverse("home:login"))


    else:
        return render(request,'home/login.html',)


    return render(request,'home/login.html',)


def about(request):
    return render(request,'home/about.html',)

@login_required
def profile(request):
    return render(request,'home/profile.html',)


@login_required
def Image_Upload(request):
    userprofile = request.user.userprofile
    imageform = forms.Upload_Image(instance = userprofile)

    if request.method == "POST":
        imageform = forms.Upload_Image(request.POST, request.FILES, instance = userprofile)

        if imageform.is_valid():

            imageform.save()
            #print("image name is ",x.image)

            return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/uploadedpic.html',{'image':imageform})


@login_required
def Update_Details(request):
    userform = forms.UpdateUser(instance = request.user)
    addressform = forms.UploadAddress(instance = request.user.useraddress)

    if request.method == "POST":
        addressform = forms.UploadAddress(data = request.POST,instance = request.user.useraddress)
        userform = forms.UpdateUser(data = request.POST, instance = request.user)

        if userform.is_valid() and addressform:

            userform.save()
            addressform.save()

            return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/update_details.html',{'userform':userform,'addressform':addressform})
