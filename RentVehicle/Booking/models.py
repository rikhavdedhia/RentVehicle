from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from Vehicle.models import Vehicle
from dropdowndb.models import BookingStatus, RequestStatus

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    bookingDate = models.DateField()
    bookingDoneOn = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=6,decimal_places = 2)
    additionalDriverName = models.CharField(max_length=256,null=True)
    additionalDriverLicense = models.CharField(max_length=15,null=True)
    requestStatus = models.ForeignKey(RequestStatus, on_delete=models.CASCADE,null=True)
    bookingStatus = models.ForeignKey(BookingStatus, on_delete=models.CASCADE,null=True)
    negotiationRequest = models.BooleanField(default=False)
    negotiationPrice = models.DecimalField(max_digits=6,decimal_places = 2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "Booking:RenterBookingDetails",
            kwargs={
                "pk": self.pk
            }
        )

class PaymentDetailsCard(models.Model):
    cardHolderName = models.CharField(max_length=256)
    cardNumber = models.PositiveIntegerField()
    cardCVV = models.PositiveIntegerField()
    expDate = models.CharField(max_length=5)
    zipCode = models.CharField(max_length=5)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return self.cardHolderName

    def get_absolute_url(self):
        return reverse(
            "Booking:RenterBookingDetails",
            kwargs={
                "pk": self.booking.pk
            }
        )

class PaymentDetailsCheck(models.Model):
    Bank = models.CharField(max_length=256)
    CheckNumber = models.PositiveIntegerField()
    RoutingNumber = models.PositiveIntegerField()
    CheckDate = models.CharField(max_length=5)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return self.cardHolderName

    def get_absolute_url(self):
        return reverse(
            "Booking:RenterBookingDetails",
            kwargs={
                "pk": self.booking.pk
            }
        )
