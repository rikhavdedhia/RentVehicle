from Vehicle import models
from . import models as omodels
from django import forms

class VehicleCreate(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        exclude = ['user','rating']

class AcceptRejectForm(forms.ModelForm):
    class Meta:
        model = omodels.AcceptRejectBooking
        fields = ['value']

class GetFeedback(forms.ModelForm):
    class Meta:
        model = omodels.RenterFeedback
        fields = ['rating','description']

class AccidentReport(forms.ModelForm):
    class Meta:
        model = models.Accident
        fields = ['disabled','description']
