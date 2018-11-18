from django.shortcuts import render
from .models import BloodAvailability
from home.models import UserAddress
from django.core.mail import send_mail


# Create your views here.


# This function is only for generating the availability list
def index(request):
    availability = BloodAvailability.objects.all()
    Availability = {'available': availability}

    return render(request, "stock/index.html", context=Availability)


# This function generates array of emails needed to be notified
# and accessing the userdata for checking his bloodgroup


def sendingmail(request):
    Availability = BloodAvailability.objects.all()

    for availability in Availability:
        if availability.bloodgroup_A_minus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            a_minus = 'A-'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that A- blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_A_plus < availability.threshhold:
            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            a_plus = 'A+'
            Donor_data_selected = UserAddress.objects.filter(blood=a_plus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that A+ blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_B_minus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            b_minus = 'B-'
            Donor_data_selected = UserAddress.objects.filter(blood=b_minus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that B- blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_B_plus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            b_plus = 'B+'
            Donor_data_selected = UserAddress.objects.filter(blood=b_plus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that B+ blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_O_minus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            o_minus = 'O-'
            Donor_data_selected = UserAddress.objects.filter(blood=o_minus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that O- blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_O_plus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            o_plus = 'O+'
            Donor_data_selected = UserAddress.objects.filter(blood=o_plus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that O+ blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_AB_minus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            ab_minus = 'AB-'
            Donor_data_selected = UserAddress.objects.filter(blood=ab_minus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that AB- blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

        if availability.bloodgroup_AB_plus < availability.threshhold:

            Donor_data = UserAddress.objects.all()
            print(Donor_data)
            ab_plus = 'AB+'
            Donor_data_selected = UserAddress.objects.filter(blood=ab_plus)
            print(Donor_data_selected)
            for user in Donor_data_selected:
                # Email_List.append(user.user.email)
                print(user.user.email)
                send_mail(
                    'Notification regarding blood donation ',
                    'It is to be notified that AB+ blood qty is less in our blood bank we need your help',
                    'vedavyas22541@gmail.com',
                    [user.user.email, ],
                )

    return render(request, "stock/mail.html")
