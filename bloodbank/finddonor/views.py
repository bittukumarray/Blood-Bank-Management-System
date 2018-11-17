import datetime

from django.shortcuts import render
from home.models import UserAddress, UserHistory
from .forms import BloodForm
from home.models import *
from django.http import HttpResponseRedirect, HttpResponse

def load_cities(request):
    print("sdhksdsknsl")
    state_id = request.POST.get('state')
    print(state_id)
    cities = City.objects.filter(state_id=state_id).order_by('name')
    print(cities)
    return render(request, 'finddonor/dropdown.html', {'cities': cities})

def index(request):
    sorry = ''
    result = ''
    if request.method == 'POST':
        form = BloodForm(request.POST)

        if form.is_valid():
            blood = form.cleaned_data['blood']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            result = UserAddress.objects.filter(blood=blood, city=city,state=state)
            queryset = UserAddress.objects.none()
            # print(result)
            for donor in result:
                a = UserHistory.objects.filter(user=donor.user)
                if a[0].donation_date:
                    if (datetime.date.today() - a[0].donation_date.date()).days > 90:
                        queryset |= UserAddress.objects.filter(user=donor.user)

            print(queryset)
            context = {'result': queryset, 'form': form}

            return render(request, 'finddonor/index.html', context)

    else:
        form = BloodForm()

    return render(request, 'finddonor/index.html', {'form': form})

