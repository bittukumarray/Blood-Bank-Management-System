from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from .forms import RequestorForm
from .models import Requestor
from home.models import *
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from datetime import date


# Create your views here.

def index(request,req_blood):
    current_site = get_current_site(request)
    if request.method == 'POST':
        form = RequestorForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            reason = form.cleaned_data['reason']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']

            blood = request.POST.get('blood')
            print(blood)

            if UserAddress.objects.filter(blood=blood, city=city, state=state, ).count() == 0:
                return render(request, 'requestblood/sorry.html', {'error': 'Sorry.no donor found near you!'})

            print(date.today())
            print(date)
            if Requestor.objects.filter(name= name,phone=phone,date=date.today()).exists():
                return render(request, 'requestblood/sorry.html', {'error': 'Your request has already been sent. Please wait for donor\'s response'})

            else:
                requestor = Requestor.objects.create(name=name, blood=blood, phone=phone, email=email, reason=reason)
                # print(requestor.email)
                query = UserAddress.objects.filter(blood=blood, city=city)
                result = UserAddress.objects.none()
                #print(query)
                for donor in query:
                    a = UserHistory.objects.filter(user=donor.user)
                    if (datetime.date.today() - a[0].donation_date.date()).days > 90:
                        result |= a
                # print((datetime.date.today()-a.donation_date.date()).days)
                #print(result)
                subject = 'Request for blood'
                # print(message)
                from_email = requestor.email
                # to_email = []
                for donor in result:
                    #print(donor.user.username)
                    to_email = [donor.user.email, ]
                    # message = 'Hello,' + donor.user.username + '!' + requestor.name + ' has requested you for blood donation as he has ' + requestor.reason + \
                    #           '.Could you help him, please? His contact details are:\nPhone no.: ' + requestor.phone + \
                    #           '\nEmail: ' + requestor.email + '\nLooking forward to a positive response. Thanks in advance'
                    #
                    # print(message)
                    # #{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
                    #print(current_site.domain)
                    link = 'http://' + current_site.domain + '/donate/'
                    #print(link)
                    context = {
                        'link': link,
                        'username': donor.user.username,
                        'requestor': requestor.name,
                        'reason' : requestor.reason,
                        'phone' : requestor.phone,
                        'email' : requestor.email,

                    }
                    message = render_to_string('requestblood/email.html', context)
                    msg = EmailMessage(subject, message, to=[to_email], from_email=from_email)
                    msg.content_subtype = 'html'
                    # msg.send()
                    try:
                        # send_mail(
                        #     subject,
                        #     message,
                        #     from_email,
                        #     to_email,
                        #     fail_silently=False
                        # )
                        msg.send()
                        print('Successful')
                    except:
                        print('\nUnsuccessful attempt')
                        return render(request, 'requestblood/sorry.html',
                                      {'error': 'There was an error in sending the email'})

                return render(request,'requestblood/response.html')

    else:
        form = RequestorForm()

    return render(request, 'requestblood/index.html', {'form': form,'blood':req_blood})


def sorry(request):
    return render(request, 'requestblood/sorry.html')


def response(request):
    return render(request, 'requestblood/response.html')


def redi(request):
    return redirect('availability:index')