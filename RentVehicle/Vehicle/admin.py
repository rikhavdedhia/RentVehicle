from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Vehicle)
admin.site.register(models.Filter)
admin.site.register(models.Accident)
