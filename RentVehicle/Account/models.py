from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Renter(models.Model):
    #This uses the authentication model defined in Django.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256,blank=True)
    street_add = models.CharField(max_length=256)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    license = models.CharField(max_length=15)

    def __str__(self):
        return '@{}'.format(self.user.username)

    class Meta():
        ordering = ['name']

class Owner(models.Model):
    #This uses the authentication model defined in Django.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256,blank=True)
    street_add = models.CharField(max_length=256)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    license = models.CharField(max_length=15)

    def __str__(self):
        return '@{}'.format(self.user.username)

    class Meta():
        ordering = ['name']
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if (instance = user.renter):
#         instance.renter.save()
#     # else:
#     #     instance.owner.save()
