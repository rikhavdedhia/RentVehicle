# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
from . import models
from django import forms
import datetime
from Vehicle import models as vmodels
from dropdowndb import models as dmodels

class CreateBooking(forms.ModelForm):
    class Meta:
        fields = ('bookingDate','additionalDriverName','additionalDriverLicense','negotiationPrice')
        model = models.Booking

    def __init__(self,*args,**kwargs):
        self.vehNum = kwargs.pop('VehNum')
        self.user = kwargs.pop('user')
        super(CreateBooking,self).__init__(*args, **kwargs)
        self.fields['bookingDate'].initial = vmodels.Filter.objects.get(user=self.user).bookingDate
        self.fields['additionalDriverName'].required = False
        self.fields['additionalDriverLicense'].required = False
        self.fields['negotiationPrice'].required = False

    def clean_bookingDate(self):
        print("Cleaning Booking")
        bookingdate = self.cleaned_data.get('bookingDate')
        if(bookingdate < datetime.date.today()):
            raise forms.ValidationError("Booking date has to be future date")

        past_booking = models.Booking.objects.filter(
            vehicle= vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.vehNum)
        ).filter(
            bookingDate=bookingdate
        ).filter(
            bookingStatus = dmodels.BookingStatus.objects.get(statusId = 3)
        )
        if past_booking.count()>0:
            raise forms.ValidationError("Vehicle not available on this date")
        return bookingdate

class CreateCardPayment(forms.ModelForm):
    class Meta:
        exclude = ['booking']
        model = models.PaymentDetailsCard

class CreateCheckPayment(forms.ModelForm):
    class Meta:
        exclude = ['booking']
        model = models.PaymentDetailsCheck
