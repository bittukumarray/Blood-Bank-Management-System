from django.shortcuts import render
from .models import UserAddress
from django.http import HttpResponse


def index(request):
   return render(request, 'finddonor/index.html')
    #return HttpResponse("<h2>It worked dude !</h2>")

def detail(request):
    bloo = request.POST.get('blood')
    # print(bloo)
    result = UserAddress.objects.filter(blood=bloo)
    context = {
        'result': result,
    }
    return render(request, 'finddonor/detail.html', context)

