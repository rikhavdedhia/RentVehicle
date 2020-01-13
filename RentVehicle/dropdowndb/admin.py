from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Color)
admin.site.register(models.Make)
admin.site.register(models.MakeModel)
admin.site.register(models.State)
admin.site.register(models.Style)
admin.site.register(models.ZipCode)
admin.site.register(models.tempZipcode)
admin.site.register(models.Rating)
admin.site.register(models.BookingStatus)
admin.site.register(models.RequestStatus)
admin.site.register(models.AcceptRejectBooking)
admin.site.register(models.StateTax)
