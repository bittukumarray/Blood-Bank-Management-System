from .models import *
from django import forms


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = BloodVolunteer
        fields = '__all__'


class newcamp(forms.ModelForm):
    class Meta:
        model = BloodCamp
        fields = ('campid', 'startdate', 'enddate', 'location')


class newdonor(forms.ModelForm):
    class Meta:
        model = BloodCampDonor
        fields = '__all__'
