from django.forms import ModelForm
from home.models import UserAddress

class BloodForm(ModelForm):
    class Meta:
        model=UserAddress
        fields=['blood','city']