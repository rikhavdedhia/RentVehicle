from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state

class ZipCode(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.zipcode

class Make(models.Model):
    make = models.CharField(max_length=15)

    def __str__(self):
        return self.make

class MakeModel(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    makemodel = models.CharField(max_length=25)

    def __str__(self):
        return self.makemodel

class Color(models.Model):
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.color

class Style(models.Model):
    style = models.CharField(max_length=15)

    def __str__(self):
        return self.style

class tempZipcode(models.Model):
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.zipcode

class Rating(models.Model):
    rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.rating)

class RequestStatus(models.Model):
    statusId = models.PositiveIntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status

class BookingStatus(models.Model):
    statusId = models.PositiveIntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status

class AcceptRejectBooking(models.Model):
    value = models.CharField(max_length=25)

    def __str__(self):
        return self.value

class StateTax(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=5,decimal_places = 4)

    def __str__(self):
        return self.state.state + " " + str(self.rate)
