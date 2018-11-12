from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RequestorForm
from home.models import Requestor, UserAddress
from django.core.mail import send_mail
from django.conf import settings


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
                return render(request, 'requestblood/sorry.html', {'error': 'Sorry.no donor found near you!'})
                # return HttpResponseRedirect(reverse('request:sorry'))

            else:
                requestor = Requestor.objects.create(name=name, blood=blood, phone=phone, email=email, reason=reason)
                # print(requestor.email)
                result = UserAddress.objects.filter(blood=blood, city=city)
                subject = 'Request for blood'
                # print(message)
                from_email = requestor.email
                # to_email = []
                for donor in result:
                    print(donor.user.username)
                    to_email = [donor.user.email, ]
                    message = 'Hello,' + donor.user.username + '!' + requestor.name + ' has requested you for blood donation as he has ' + requestor.reason + \
                              '.Could you help him, please? His contact details are:\nPhone no.: ' + requestor.phone + \
                              '\nEmail: ' + requestor.email + '\nLooking forward to a positive response. Thanks in advance'

                    print(message)
                    try:
                        send_mail(
                            subject,
                            message,
                            from_email,
                            to_email,
                            fail_silently=False
                        )
                    except:
                        print('\nUnsuccessful attempt')
                        return render(request, 'requestblood/sorry.html',
                                      {'error': 'There was an error in sending the email'})

                return redirect('requestblood:response')

    else:
        form = RequestorForm()

    return render(request, 'requestblood/index.html', {'form': form})


def sorry(request):
    return render(request, 'requestblood/sorry.html')


def response(request):
    return render(request, 'requestblood/response.html')

