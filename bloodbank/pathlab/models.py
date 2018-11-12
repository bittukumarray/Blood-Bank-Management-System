from django.db import models
from django import forms
from django.contrib.auth.models import User

Path_labs = (
    ('Chennai', 'Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Patna', 'Patna'),
    ('Mumbai', 'Mumbai'),
    ('Hyderabad', 'Hyderabad'),
    ('Kolkata', 'Kolkata'),
    ('Delhi', 'Delhi'),
    ('Jamshedpur', 'Jamshedpur'),
)


class PathLabs(models.Model):
    pathlabid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20, choices=Path_labs)
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=1000, blank=False)
    ratings = models.IntegerField(default=0)


class PathLabUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pathlab = models.ForeignKey(PathLabs, on_delete=models.CASCADE)
    note = models.CharField(blank=False, max_length=1000)
    feedback = models.CharField(blank=True, max_length=1000)
