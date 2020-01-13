from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Owner)
admin.site.register(models.Renter)
