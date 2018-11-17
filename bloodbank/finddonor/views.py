import datetime

from django.shortcuts import render
from home.models import UserAddress, UserHistory
from .forms import BloodForm
from home.models import *
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    sorry = ''
    result = ''
    if request.method == 'POST':
        form = BloodForm(request.POST)

        if form.is_valid():
            blood = form.cleaned_data['blood']
            city = form.cleaned_data['city']
            # if UserAddress.objects.filter(blood=blood, city=city).count() == 0:
            #     sorry = 'Sorry! No donors found !'
            #
            #
            # else:
            # a=UserHistory.objects.get(user=donor.user)
            result = UserAddress.objects.filter(blood=blood, city=city, )
            queryset = UserAddress.objects.none()
            # print(result)
            for donor in result:
                a = UserHistory.objects.filter(user=donor.user)
                if (datetime.date.today() - a[0].donation_date.date()).days > 90:
                    queryset |= a
            # print((datetime.date.today()-a.donation_date.date()).days)
            # try:
            #     print(len(queryset))
            # except:
            #     print('Unsuccesful')
            print(queryset)
            # if queryset.count() == 0:
            #     sorry = 'Sorry! No donors found !'
            context = {'result': queryset, 'form': form}

        return render(request, 'finddonor/index.html', context)

    else:
        form = BloodForm()

    return render(request, 'finddonor/index.html', {'form': form})


def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'finddonor/dropdown.html', {'cities': cities})
