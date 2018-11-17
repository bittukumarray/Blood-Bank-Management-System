from datetime import date

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django import forms
from bloodcamp.forms import newdonor, newcamp
from . import forms
from .models import *


# Create your views here.

def Volunteering(request):
    volunteerform = forms.VolunteerForm()
    if request.method == "POST":
        volunteerform = forms.VolunteerForm(data=request.POST)
        if volunteerform.is_valid():
            volunteerform.save()

            return HttpResponseRedirect(reverse('home:index'))
    return render(request, 'bloodcamp/volunteerform.html', {'volunteer': volunteerform})


def VolunteerList(request):
    obj = BloodVolunteer.objects.all()
    return render(request, 'bloodcamp/volunteer_list.html', {'volunteer': obj})


def index(request):
    return render(request, 'bloodcamp/index.html')


def camphome(request):
    return render(request, 'bloodcamp/camphome.html')


def checkdate(o):
    if (date.today() > o.enddate):
        print('check 1')
        return '1'
    elif (date.today() < o.startdate):
        print('check 3')
        return '3'
    else:
        print('check 2')
        return '2'


def default_fun(request):
    camps = BloodCamp.objects.all()
    for camp in camps:
        if checkdate(camp) == '1':
            print('is 1')
            camp.status = '1'
            camp.save()
        elif checkdate(camp) == '2':
            print('is 2')
            camp.status = '2'
            camp.save()
        elif checkdate(camp) == '3':
            print('is 3')
            camp.status = '3'
            camp.save()


def history(request):
    default_fun(request)

    camps = BloodCamp.objects.filter(status='1')
    donors = BloodCampDonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.BloodCamp.campid == camp.campid:
                    print(donor.firstname)

    # print('camps:',camps)
    # print('donors:',donors)
    content = {
        'camps': camps,
        'donors': donors,
    }
    return render(request, 'bloodcamp/history.html', context=content)


def ongoing(request):
    default_fun(request)

    camps = BloodCamp.objects.filter(status=2)
    donors = BloodCampDonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    # print('camps:',camps)
    # print('donors:',donors)
    content = {
        'camps': camps,
        'donors': donors,
    }
    return render(request, 'bloodcamp/ongoing.html', context=content)


def upcoming(request):
    default_fun(request)

    camps = BloodCamp.objects.filter(status=3)
    donors = BloodCampDonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    # print('camps:',camps)
    # print('donors:',donors)
    content = {
        'camps': camps,
        'donors': donors,
    }

    return render(request, 'bloodcamp/upcoming.html', context=content)


def newcamppage(request):
    form = newcamp()
    if request.method == 'POST':
        form = newcamp(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return camphome(request)
        else:
            print('form invalid')
    return render(request, 'bloodcamp/newcamp.html', {'form': form})


def newdonorpage(request):
    form1 = newdonor()
    if request.method == 'POST':
        form1 = newdonor(request.POST)
        if form1.is_valid():
            form1.save(commit=True)
            firstname = form1.cleaned_data['firstname']
            lastname = form1.cleaned_data['lastname']
            phone = form1.cleaned_data['phone']
            blood = form1.cleaned_data['blood']
            email = str(form1.cleaned_data['email'])
            bloodcamp = form1.cleaned_data['bloodcamp']
            #message = 'Dear ' + firstname + ", You have registered for the blood donation camp at "+ bloodcamp + ""
            send_mail(
                'Blood Bank',
                'FirstName:' + str(firstname) + '\n' +
                'Lastname:' + str(lastname) + '\n' +
                'Phone:' + str(phone) + '\n' +
                'Blood:' + str(blood) + '\n' +
                'bloodcamp:' + str(bloodcamp) + '\n',
                '29riyajain@gmail.com',
                [email],
                fail_silently=False,
            )

            return camphome(request)
        else:
            print('form invalid')
    return render(request, 'bloodcamp/newdonor.html', {'form1': form1})
