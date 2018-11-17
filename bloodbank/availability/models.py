from django.db import models

Blood_Groups = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)


# Create your models here.
class BloodAvailability(models.Model):
    threshold = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    blood = models.CharField(max_length=10, choices=Blood_Groups)

    def __str__(self):
        return self.blood;
    # A_plus = models.IntegerField(default=0)
    # A_minus = models.IntegerField(default=0)
    # B_plus = models.IntegerField(default=0)
    # B_minus = models.IntegerField(default=0)
    # O_plus = models.IntegerField(default=0)
    # O_minus = models.IntegerField(default=0)
    # AB_plus = models.IntegerField(default=0)
    # AB_minus = models.IntegerField(default=0)
