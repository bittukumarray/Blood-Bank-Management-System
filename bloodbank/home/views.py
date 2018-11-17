from django.shortcuts import render, redirect
from .models import *
from . import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.cache import never_cache
#from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import render, Http404
from django.contrib.auth import update_session_auth_hash
from credits.models import Wallet, Transaction
from django.contrib.auth.views import PasswordResetView

#def my_password_reset(request,template_name="home/volunteerform.html"):
#    return PasswordResetView(request,template_name)


# Create your views here.

def index(request):
    return render(request,'home/index.html')

def SignUp(request):

    userform=forms.UserForm()
    useraddressform=forms.UserAddressForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home:profile"))

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
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home:profile"))

    elif request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # if user:
        #     if user.is_active:
        #         login(request,user)
        #
        #
        #
        #         return HttpResponseRedirect(reverse("home:index"))

        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    print('Lalalala')
                    return redirect(request.POST.get('next'))
                else:
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
    try:
        userprofile = request.user.userprofile
    except:
        return HttpResponseRedirect(reverse('home:profile'))

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
    try:
        addressform = forms.UploadAddress(instance = request.user.useraddress)
    except:
        return HttpResponseRedirect(reverse('home:profile'))

    if request.method == "POST":
        addressform = forms.UploadAddress(data = request.POST,instance = request.user.useraddress)
        userform = forms.UpdateUser(data = request.POST, instance = request.user)

        if userform.is_valid() and addressform:

            userform.save()
            addressform.save()

            return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/update_details.html',{'userform':userform,'addressform':addressform})

@login_required
def Update_Password(request):
    if request.method == "POST":
        #passwordform = forms.PasswordForm(data = request.POST, instance=request.user)
        #return HttpResponseRedirect(reverse('home:update_password'))
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = authenticate(username=request.user.username,password=password)
        form=request.user

        if user:
            print(user)
            if new_password == confirm_password:
                print(new_password==confirm_password)
                curuser=request.user
                #curuser.password=new_password
                curuser.set_password(new_password)
                curuser.save()
                update_session_auth_hash(request, form)
                return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/password.html',)







#def password_change(request):
#    if request.method == 'POST':
#        form = PasswordChangeForm(user=request.user, data=request.POST)
#        if form.is_valid():
#            form.save()
#            update_session_auth_hash(request, form.user)
