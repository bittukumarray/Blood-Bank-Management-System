from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from .models import BloodAvailability
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.http import HttpResponse


# Create your views here.

def index(request):
    quantity = BloodAvailability.objects.all()
    context = {
        'quantity': quantity
    }
    return render(request, 'availability/index.html', context)


# def send(request):
#     current_site = get_current_site(request)
#     try:
#         subject, from_email, to = 'hello', 'riyashachijain@gmail.com', 'riyashachijain@gmail.com'
#         text_content = 'This is an important message.'
#         html_content = '<p>This is an <strong>important</strong> message.</p>'
#         link = 'http://' + current_site.domain + '/home/'
#         print(link)
#         context = {
#             'link': link
#         }
#         message = render_to_string('availability/send.html',context)
#         msg = EmailMessage(subject, message, to=[to], from_email=from_email)
#         msg.content_subtype = 'html'
#         msg.send()
#         # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#         # msg.attach_alternative(html_content, "text/html")
#         # msg.send()
#         print('Succesful')
#     except:
#         print('Unsuccessful')
#
#     return HttpResponse('<h2>Done</h2>')
