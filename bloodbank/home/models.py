from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

Blood_Groups = (
    ('A+','A-'),
    ('A-', 'A+'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+', 'AB+'),
    ('AB-','AB-'),
)

Path_labs = (
    ('Chennai','Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Patna','Patna'),
    ('Mumbai','Mumbai'),
    ('Hyderabad','Hyderabad'),
    ('Kolkata','Kolkata'),
    ('Delhi', 'Delhi'),
    ('Jamshedpur','Jamshedpur'),
)



Gender = (
    ('male','Male'),
    ('female', 'Female'),
    ('transgender', 'Transgender'),
)

States = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('karnataka', 'karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Goa', 'Goa'),
    ('Telangana', 'Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),


)



class UserAddress(models.Model):
    useraddressid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    state = models.CharField(max_length = 30, choices=States)
    city = models.CharField(blank = False, null = False, max_length = 200)
    phone = models.CharField(blank = False, null = False, max_length = 100)
    birth = models.CharField(blank = False, null = False, max_length = 200)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now_add = True)
    blood = models.CharField(max_length=10, choices=Blood_Groups)

class UserProfile(models.Model):
    userprofileid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    #donoraddress = models.OneToOneField(DonorAddress,on_delete = models.CASCADE)
    status = models.CharField(null = True, max_length = 200)
    feedback = models.CharField(null = True, max_length = 1000)


class UserHistory(models.Model):
    userhistoryid = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    #username=models.CharField(max_length =200, null = False, blank = False)
    donation_date = models.DateTimeField(auto_now = True, auto_now_add = False)

# Donor's Wallet

class Wallet(models.Model):
    walletid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    credit = models.IntegerField(default = 0)

class Transaction(models.Model):
    transactionid = models.AutoField(primary_key = True)
    wallet = models.ForeignKey(Wallet, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    initialcredit = models.IntegerField(null = True, blank = True)
    aftercredit = models.IntegerField(null = True, blank = True)
    getcredit = models.IntegerField(null = True)
    pathlab = models.CharField(max_length=20, choices=Path_labs)
    def updatewallet(self):
        self.wallet.credit = self.wallet.credit + self.getcredit


#Blood Donation Camp

class BloodAvailability(models.Model):
    threshhold = models.IntegerField(default = 0)
    bloodgroup_A_plus = models.IntegerField(default = 0)
    bloodgroup_A_minus = models.IntegerField(default = 0)
    bloodgroup_B_plus = models.IntegerField(default = 0)
    bloodgroup_B_minus = models.IntegerField(default = 0)
    bloodgroup_O_plus = models.IntegerField(default = 0)
    bloodgroup_O_minus = models.IntegerField(default = 0)
    bloodgroup_AB_plus = models.IntegerField(default = 0)
    bloodgroup_AB_minus = models.IntegerField(default = 0)




class BloodCamp(models.Model):
    place = models.CharField(blank=False, null = False, max_length = 100)
    duration = models.CharField(blank = False, max_length = 200, null = False)

class BloodCampDonor(models.Model):
    name = models.CharField(blank=False, null = False, max_length=100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 11, blank = True)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now_add = True)
    blood = models.CharField(max_length=10, choices=Blood_Groups)
    bloodcamp = models.ForeignKey(BloodCamp,on_delete = models.CASCADE)
