from django.shortcuts import render, Http404

# Create your views here.

def hello(request):
    raise Http404('Hello')
