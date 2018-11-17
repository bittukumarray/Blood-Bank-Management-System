from django.shortcuts import render
from .models import PathLabUser, PathLabs
from .forms import PathlabForm
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    result = ''
    if request.method == 'POST':
        form = PathlabForm(request.POST)

        if form.is_valid():
            testtype = form.cleaned_data['testtype']

            result = PathLabUser.objects.filter(testtype=testtype)
            context = {'result': result, 'form': form, }
            return render(request, 'pathlab/index.html', context)


    else:
        form = PathlabForm()
    return render(request, 'pathlab/index.html', {'form': form})


def result(request):
    return render(request, 'pathlab/result.html')
