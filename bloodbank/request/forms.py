from django.forms import ModelForm
from home.models import Requestor


class RequestorForm(ModelForm):
    class Meta:
        model = Requestor
        fields = ['name', 'blood', 'city','phone', 'email', 'reason']
