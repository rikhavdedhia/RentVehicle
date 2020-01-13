from django.db import models
from dropdowndb import models as dmodels
from Vehicle.models import Vehicle
from django.contrib.auth.models import User
from Booking.models import Booking
from django.urls import reverse

# Create your models here.
class AcceptRejectBooking(models.Model):
    value = models.ForeignKey(dmodels.AcceptRejectBooking, on_delete=models.CASCADE)

class RenterFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,null=True)
    rating = models.ForeignKey(dmodels.Rating, on_delete=models.CASCADE,null=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('Owner:OwnerVehicles')
