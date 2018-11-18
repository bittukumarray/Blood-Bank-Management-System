from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Hospital
from django.urls import reverse_lazy


def hospitals(request):
    hospitals = Hospital.objects.all()
    #template = loader.get_template('Hospitals/index.html')
    context = {'hospitals': hospitals, }
    #return render(request, 'Hospitals/index.html', )
    return render(request, 'Hospitals/index.html', context)

def result(request):
    return render(request,'Hospitals/result.html')

