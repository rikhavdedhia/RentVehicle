from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import generic
from Vehicle import models
from Booking import models as bmodels
from . import forms
from django.http import Http404
from dropdowndb import models as dmodels
from . import models as omodels
import datetime

# Create your views here.
class ListOwnerVehicles(generic.ListView):
    model = models.Vehicle
    template_name = 'Owner/OwnerVehicle_List.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            self.vehicle = models.Vehicle.objects.filter(
                user = self.request.user
            )
            try:
                Accident_vehicle = models.Accident.objects.filter(
                    disabled = True
                ).values()
                if len(Accident_vehicle) > 0:
                    Accident_vehicle_list = []
                    for av in Accident_vehicle:
                        Accident_vehicle_list.append(av['vehicle_id'])
                    self.vehicle = self.vehicle.filter(
                        pk__in = Accident_vehicle_list
                    )
                    context['vehicle'] = self.vehicle
                return context
            except Exception as e:
                print(type(e))
                print("In except")
                return context
        except Exception as e:
            print(type(e))
            print("In except")
            return context

    def get_queryset(self):
        try:
            self.vehicles = models.Vehicle.objects.filter(
                user = self.request.user
            )
            try:
                Accident_vehicle = models.Accident.objects.filter(
                    disabled = True
                ).values()
                for av in Accident_vehicle:
                    self.vehicles = self.vehicles.exclude(
                    pk = av['vehicle_id']
                    )
            except:
                pass
        except Exception as e:
            print (type(e))
            return ""
        else:
            return self.vehicles.all()

class CreateVehicle(generic.CreateView):
    form_class = forms.VehicleCreate
    model = models.Vehicle
    template_name = "Owner/vehicle_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.rating = 0
        if 'image' in self.request.FILES:
            self.object.image = self.request.FILES['image']
            print("Here")
        self.object.save()
        return super().form_valid(form)

class VehicleDetails(generic.DetailView):
    model = models.Vehicle
    template_name = "Owner/OwnerVehicle_Detail.html"
    context_object_name = "vehicle_detail"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(
    #         VehicleRegistrationNumber = self.kwargs.get("VehicleRegistrationNumber")
    #     )
        # try:
        #     vehicle = models.Vehicle.objects.get(
        #         VehicleRegistrationNumber = self.kwargs.get("VehicleRegistrationNumber")
        #     )
        # except Exception as e:
        #     print (type(e))
        #     return ""
        # else:
        #     return self.vehicles.all()

class RequestList(generic.ListView):
    model = bmodels.Booking
    template_name = "Owner/request_list.html"
    context_object_name = 'request_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            vehicle__user = self.request.user
        )
        return queryset.filter(
            requestStatus__statusId = 1
        ).filter(
            bookingDate__gte = datetime.date.today()
        )

class RequestDetails(generic.DetailView):
    model = bmodels.Booking
    form = forms.AcceptRejectForm()
    template_name = 'Owner/request_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        try:
            booking = bmodels.Booking.objects.get(pk=self.kwargs.get('pk'))
            negotiationRequest = booking.negotiationRequest
            context["negotiationRequest"] = negotiationRequest
            feedback = omodels.RenterFeedback.objects.filter(booking__user = booking.user)
            context['feedback'] = feedback
        except:
            return context
        return context

    def post(self, request, *args, **kwargs):
        filter_form = forms.AcceptRejectForm(data = request.POST)
        if filter_form.is_valid():
            filterForm = filter_form.save(commit=False)
            booking = bmodels.Booking.objects.get(pk=self.kwargs.get('pk'))
            if filterForm.value == dmodels.AcceptRejectBooking.objects.get(pk=1):
                booking.requestStatus = dmodels.RequestStatus.objects.get(statusId=3)
            else:
                booking.requestStatus = dmodels.RequestStatus.objects.get(statusId=2)
            if self.request.POST.get('Negotiate') == 'on':
                booking.price = booking.negotiationPrice
            else:
                booking.negotiationRequest = False
            booking.save()
        return redirect('Owner:RequestList')

class OwnerFeedback(generic.CreateView):
    form_class = forms.GetFeedback
    model = omodels.RenterFeedback
    template_name = "Owner/RenterFeedback.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        BookingDetails = bmodels.Booking.objects.get(
                pk=self.kwargs.get('pk')
                )
        context['BookingDetails'] = BookingDetails
        print(BookingDetails.vehicle.VehicleRegistrationNumber)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.booking = bmodels.Booking.objects.get(
            pk = self.kwargs.get('pk')
        )
        self.object.save()
        return super().form_valid(form)

class ReportAccident(generic.CreateView):
    form_class = forms.AccidentReport
    model = models.Accident
    template_name = "Owner/ReportAccident.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = models.Vehicle.objects.get(
                pk=self.kwargs.get('pk')
                )
        context['vehicle'] = vehicle
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.vehicle = models.Vehicle.objects.get(
                pk=self.kwargs.get('pk')
                )
        self.object.save()
        return super().form_valid(form)

class EnableVehicle(generic.DetailView):
    model = models.Vehicle
    template_name = 'Owner/EnableVehicle.html'
    context_object_name = "vehicle_detail"

    def post(self, request, *args, **kwargs):
        accidentVehicle = models.Accident.objects.filter(
            vehicle__pk = self.kwargs.get("pk")
        ).filter(
            disabled = True
        )
        accidentVehicle.update(disabled = False)
        return redirect('Owner:OwnerVehicles')
