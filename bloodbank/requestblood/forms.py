from django.forms import ModelForm
from .models import Requestor


class RequestorForm(ModelForm):
    class Meta:
        model = Requestor
        fields = ['name', 'state', 'city', 'phone', 'email', 'reason']
