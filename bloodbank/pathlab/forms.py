from django import forms
from .models import PathLabs,PathLabUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse


class PathlabForm(forms.ModelForm):
    class Meta:
        model = PathLabUser
        fields = ['testtype']