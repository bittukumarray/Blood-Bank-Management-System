from django.shortcuts import render
from .models import UserAddress
from .forms import BloodForm
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    sorry = ''
    result = ''
    if request.method == 'POST':
        form = BloodForm(request.POST)

        if form.is_valid():
            blood = form.cleaned_data['blood']
            city = form.cleaned_data['city']
            if UserAddress.objects.filter(blood=blood,city=city).count() == 0:
                sorry = 'Sorry! No donors found !'
            else:
                result = UserAddress.objects.filter(blood=blood,city=city)
            context = {'result': result, 'form': form, 'sorry': sorry}
            return render(request, 'finddonor/index.html', context)

    else:
        form = BloodForm()
    return render(request, 'finddonor/index.html', {'form': form})
