#https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from . import models, forms
from django.http import Http404
from dropdowndb.models import tempZipcode, ZipCode
from django.http import HttpResponseRedirect
from Booking import models as bmodels
from dropdowndb import models as dmodels

# Create your views here.
class VehicleList(generic.ListView):
    model = models.Vehicle
    template_name = "Vehicle/vehicle_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def get_queryset(self):
        try:
            #self.vehicle = super().get_queryset()
            self.form = forms.CreateFilter()
            self.filter = models.Filter.objects.get(user=None)

            self.vehicles = models.Vehicle.objects.filter()
            try:
                Accident_vehicle = models.Accident.objects.filter(
                    disabled = True
                ).values()
                if len(Accident_vehicle) > 0:
                    for av in Accident_vehicle:
                        self.vehicles = self.vehicles.exclude(
                        pk = av['vehicle_id']
                        )
            except:
                pass
            if self.filter.zipcode:
                print('1')
                self.vehicles = self.vehicles.filter(
                    zipcode__zipcode = self.filter.zipcode
                )
            if self.filter.make:
                print('2')
                self.vehicles = self.vehicles.filter(
                    make__make = self.filter.make.make
                )
            if self.filter.color:
                print('3')
                self.vehicles = self.vehicles.filter(
                    color__color = self.filter.color
                )
            if self.filter.StartPrice and self.filter.EndPrice:
                print('4')
                print(self.filter.StartPrice)
                self.vehicles = self.vehicles.filter(
                    price__gte = self.filter.StartPrice

                ).filter(
                price__lte = self.filter.EndPrice
                )
            elif self.filter.EndPrice:
                print('5')
                self.vehicles = self.vehicles.filter(
                    price__lte = self.filter.EndPrice
                )
            elif self.filter.StartPrice:
                print('8')
                self.vehicles = self.vehicles.filter(
                    price__gte = self.filter.EndPrice
                )
            if self.filter.rating:
                print('6')
                self.vehicles = self.vehicles.filter(
                    rating__rating__gte = self.filter.rating.rating
                )
            if self.filter.style:
                print('7')
                self.vehicles = self.vehicles.filter(
                    style__style = self.filter.style
                )
            if self.filter.bookingDate:
                pk = bmodels.Booking.objects.filter(bookingDate = self.filter.bookingDate)
                pk = pk.filter(bookingStatus = dmodels.BookingStatus.objects.get(pk=3)).values()
                print('8')
                for veh in pk:
                    print(veh['vehicle_id'])
                    self.vehicles = self.vehicles.exclude(
                        pk = veh['vehicle_id']
                    )
                print('8')
        except Exception as e:
            print (type(e))
            return ""
        else:
            return self.vehicles.all()

    def post(self, request, *args, **kwargs):
        filter_form = forms.CreateFilter(data = request.POST)
        if filter_form.is_valid():
            filterForm = filter_form.save(commit=False)
            filter = models.Filter.objects.filter(user=None)
            filter.update(zipcode=filterForm.zipcode,
                          make = filterForm.make,
                          color=filterForm.color,
                          style=filterForm.style,
                          StartPrice=filterForm.StartPrice,
                          EndPrice=filterForm.EndPrice,
                          rating=filterForm.rating,
                          bookingDate=filterForm.bookingDate
                          )
        return redirect('Vehicle:all')

class VehicleDetails(generic.DetailView):
    model = models.Vehicle
    template_name = "Vehicle/Vehicle_Detail.html"
    context_object_name = "vehicle_detail"
