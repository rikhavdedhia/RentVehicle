from django.db import models
from dropdowndb.models import Color, Make, MakeModel, State, Style, ZipCode, Rating
from django.urls import reverse
from django.contrib.auth.models import User
from dropdowndb import models as dmodels

# Create your models here.
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(MakeModel, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5,decimal_places = 2)
    insurance = models.BooleanField()
    zipcode = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    description = models.TextField()
    TermsAndConditions = models.CharField(max_length=256)
    VehicleRegistrationNumber = models.CharField(max_length = 15, unique = True)
    rating = models.PositiveIntegerField(default=0)
    securityDeposit = models.DecimalField(max_digits = 6, decimal_places = 2)
    EZpass = models.BooleanField()
    image = models.ImageField(upload_to = 'car_images', blank = True)

    def __str__(self):
        return self.make.make + " " + self.model.makemodel

    def get_absolute_url(self):
        return reverse('Owner:OwnerVehicles')

    class Meta:
        ordering = ['-rating']

class Filter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    zipcode = models.CharField(max_length=5,null=True)
    make = models.ForeignKey(dmodels.Make, on_delete=models.CASCADE,null=True)
    color = models.ForeignKey(dmodels.Color, on_delete=models.CASCADE,null=True)
    StartPrice = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    EndPrice = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    rating = models.ForeignKey(dmodels.Rating, on_delete=models.CASCADE,null=True)
    style = models.ForeignKey(dmodels.Style, on_delete=models.CASCADE,null=True)
    bookingDate = models.DateField(null=True)

# class Images(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to = 'car_images', blank = True)

class Accident(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    disabled = models.BooleanField()
    description = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('Owner:OwnerVehicles')
