from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RequestorForm
from home.models import Requestor, UserAddress
from django.core.mail import send_mail


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RequestorForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            blood = form.cleaned_data['blood']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            reason = form.cleaned_data['reason']
            city = form.cleaned_data['city']

            if UserAddress.objects.filter(blood=blood, city=city).count() == 0:
                return redirect('request:sorry')
                #return HttpResponseRedirect(reverse('request:sorry'))

            else:
                requestor = Requestor.objects.create(name=name, blood=blood, phone=phone, email=email, reason=reason)

                result = UserAddress.objects.filter(blood=blood, city=city)
                for donor in result:
                    try:
                        send_mail(
                            'Request for blood',
                            'I need blood for' + {{requestor.reason}},
                            {{requestor.email}},
                            {{donor.user.email}}
                        )
                    except:
                        print('\nUnsuccessful attempt')

                #return HttpResponseRedirect(reverse('request:response'))
                return redirect('request:response')

            context = {'form': form}
            return HttpResponse('<h2>Valid data</h2>')

    else:
        form = RequestorForm()

    return render(request, 'request/index.html', {'form': form})


def sorry(request):
    return render(request, 'request/sorry.html')


def response(request):
    return render(request, 'request/response.html')
