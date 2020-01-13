from django.db import models
from Vehicle.models import Vehicle
from dropdowndb import models as dmodels
from django.contrib.auth.models import User
from Booking.models import Booking
from django.urls import reverse

# Create your models here.
class VehicleFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rating = models.ForeignKey(dmodels.Rating, on_delete=models.CASCADE,null=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('Renter:AvailableVehicles')
