from django.contrib import admin

# Register your models here.
from .models import *

# from django.contrib.auth.models import User

admin.site.register(UserAddress)
admin.site.register(UserProfile)
admin.site.register(UserHistory)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(BloodCamp)
admin.site.register(BloodCampDonor)
admin.site.register(BloodAvailability)
admin.site.register(Requestor)
