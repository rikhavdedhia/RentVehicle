from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Booking)
admin.site.register(models.PaymentDetailsCard)
admin.site.register(models.PaymentDetailsCheck)
