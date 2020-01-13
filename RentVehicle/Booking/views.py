from django.shortcuts import render, redirect
from django.views import generic
from . import models
from . import forms
from django.http import Http404
from Vehicle import models as vmodels
from Account import models as amodels
from dropdowndb import models as dmodels
from Booking import models as bmodels
from django.core.mail import send_mail,get_connection
from django.conf import settings
from django.views.generic.edit import ModelFormMixin
import datetime
from Renter import models as rmodels
from Owner import models as omodels

class CreateBooking(generic.CreateView):
    form_class = forms.CreateBooking
    model = models.Booking
    template_name = "Booking/booking_form.html"

    def get_form_kwargs(self):
        kwargs = super(CreateBooking, self).get_form_kwargs()
        #kwargs['VehNum'] = self.kwargs.get('VehicleRegistrationNumber') # the trick!
        kwargs.update({'VehNum': self.kwargs.get('VehicleRegistrationNumber')})
        kwargs.update({'user': self.request.user})
        print("in get_form_kwargs")
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["VRnum"] = self.kwargs.get('VehicleRegistrationNumber')
        print(self.kwargs.get('VehicleRegistrationNumber'))
        context["VRid"] = self.kwargs.get("pk")
        context['vehicle'] = vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.kwargs.get('VehicleRegistrationNumber'))
        return context

    def form_valid(self, form):
        print("in form_valid")
        self.object = form.save(commit=False)
        vehicle = vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.kwargs.get('VehicleRegistrationNumber'))
        self.object.vehicle = vehicle
        self.object.user = self.request.user
        veh_state = dmodels.ZipCode.objects.get(zipcode=vehicle.zipcode).state
        staterate = dmodels.StateTax.objects.get(state = veh_state)
        self.object.price = (vehicle.price * staterate.rate) + vehicle.securityDeposit
        self.object.requestStatus = dmodels.RequestStatus.objects.get(statusId = 1)
        self.object.bookingStatus = dmodels.BookingStatus.objects.get(statusId = 1)
        if self.request.POST.get('negotiate') == 'on':
            self.object.negotiationRequest = True
        else:
            self.object.negotiationRequest = False
            self.object.negotiationPrice = 0
        self.object.save()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     book_form = forms.CreateBooking(data = request.POST)
    #     if book_form.is_valid():
    #         self.object = book_form.save(commit=False)
    #         self.object.user = self.request.user
    #         vehicle = vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.kwargs.get('VehicleRegistrationNumber'))
    #         self.object.vehicle = vehicle
    #         self.object.price = vehicle.price + vehicle.securityDeposit
    #         self.object.requestStatus = dmodels.RequestStatus.objects.get(statusId = 1)
    #         self.object.bookingStatus = dmodels.BookingStatus.objects.get(statusId = 1)
    #         self.object.save()
    #     return redirect('Booking:BookingList')

class RenterBookingList(generic.ListView):
    model = models.Booking
    template_name = 'Booking/RenterBooking_List.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AcceptedBooking'] = models.Booking.objects.filter(
                user = self.request.user
            ).filter(
                requestStatus = dmodels.RequestStatus.objects.get(pk=3)
            ).filter(
                bookingStatus = dmodels.BookingStatus.objects.get(pk=1)
            ).filter(
                bookingDate__gte = datetime.date.today()
            )
        context['RejectedBookingOwner'] = models.Booking.objects.filter(
                user = self.request.user
            ).filter(
                requestStatus = dmodels.RequestStatus.objects.get(pk=2)
            ).filter(
                bookingDate__gte = datetime.date.today()
            )
        context['RejectedBookingRenter'] = models.Booking.objects.filter(
                user = self.request.user
            ).filter(
                requestStatus = dmodels.RequestStatus.objects.get(pk=3)
            ).filter(
                bookingStatus = dmodels.BookingStatus.objects.get(pk=2)
            ).filter(
                bookingDate__gte = datetime.date.today()
            )
        context['CompletedBooking'] = models.Booking.objects.filter(
                user = self.request.user
            ).filter(
                requestStatus = dmodels.RequestStatus.objects.get(pk=3)
            ).filter(
                bookingStatus = dmodels.BookingStatus.objects.get(pk=3)
            ).filter(
                bookingDate__gte = datetime.date.today()
            ).filter(
                bookingDate__gte = datetime.date.today()
            )
        context['OldBooking'] = models.Booking.objects.filter(
                user = self.request.user
            ).filter(
                requestStatus = dmodels.RequestStatus.objects.get(pk=3)
            ).filter(
                bookingStatus = dmodels.BookingStatus.objects.get(pk=3)
            ).filter(
                bookingDate__lte = datetime.date.today()
            )
        return context

    def get_queryset(self):
        try:
            self.bookings = bmodels.Booking.objects.filter(
                user = self.request.user
            ).filter(
                requestStatus = dmodels.RequestStatus.objects.get(pk=1)
            ).filter(
                bookingDate__gte = datetime.date.today()
            )
        except Exception as e:
            print (type(e))
            return ""
        else:
            return self.bookings.all()

class OwnerBookingList(generic.ListView):
    model = models.Booking
    template_name = 'Booking/OwnerBooking_List.html'

    def get_queryset(self):
        try:
            self.bookings = bmodels.Booking.objects.filter(
                vehicle__user = self.request.user
            )
            self.bookings = self.bookings.filter(
                bookingStatus = dmodels.BookingStatus.objects.get(pk=3)
            )
        except Exception as e:
            print (type(e))
            return ""
        else:
            return self.bookings.all()

class RenterBookingDetails(generic.DetailView):
    model = models.Booking
    template_name = "Booking/renterBooking_Detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        if booking.requestStatus == dmodels.RequestStatus.objects.get(pk=3):
            context["Owneraccepted"] = True
        else:
            context["Owneraccepted"] = False
        if booking.bookingStatus == dmodels.BookingStatus.objects.get(pk=2):
            context["renterRejected"] = False
        else:
            context["renterRejected"] = True
        if booking.bookingStatus == dmodels.BookingStatus.objects.get(pk=3):
            context["booked"] = True
        else:
            context["booked"] = False
        return context

    def post(self, request, *args, **kwargs):
        booking = models.Booking.objects.filter(pk=self.kwargs.get('pk'))
        booking.update(bookingStatus = dmodels.BookingStatus.objects.get(pk=2))
        return redirect('Booking:RenterBookingList')

class SelectPayment(generic.DetailView):
    template_name = 'Booking/SelectPayment.html'
    model = models.Booking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        context["pk"] = booking.pk
        return context

class CardPayment(generic.CreateView):
    form_class = forms.CreateCardPayment
    model = models.PaymentDetailsCard
    template_name = "Booking/Card_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        curr_booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        curr_booking.bookingStatus = dmodels.BookingStatus.objects.get(statusId=3)
        curr_booking.save()
        self.object.booking = curr_booking
        self.object.save()
        EmailSender(curr_booking,[curr_booking.user.email],[curr_booking.vehicle.user.email])
        return super().form_valid(form)

class CheckPayment(generic.CreateView):
    form_class = forms.CreateCheckPayment
    model = models.PaymentDetailsCheck
    template_name = "Booking/Check_form.html"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        curr_booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        curr_booking.bookingStatus = dmodels.BookingStatus.objects.get(statusId=3)
        curr_booking.save()
        self.object.booking = curr_booking
        self.object.save()
        EmailSender(curr_booking)
        return super().form_valid(form)

def EmailSender(curr_booking,RenterEmail,OwnerEmail):
    my_use_tls = True
    my_host = "smtp.gmail.com"
    my_user = "rentvehicle2019@gmail.com"
    my_password = "Qwe123rty!"
    my_port = 587

    new_conn = get_connection(host=my_host,port=my_port,username=my_user,password=my_password,use_tls=my_use_tls)

    subject = 'Booking Confirmation'
    message_renter = 'Thank you for renting the car. Following are the booking details: -\nCar: - {}\nBooking Date: - {}\nBooking Price: - {}\n'.format(curr_booking.vehicle,curr_booking.bookingDate,curr_booking.price)
    message_owner = 'Booking are the details for the booking done for your car: -\nCar: - {}\nBooking Date: - {}\nBooking Price: - {}\nAmount creditted to you is: -{}'.format(curr_booking.vehicle,curr_booking.bookingDate,curr_booking.price,str(round(int(curr_booking.price)*0.9,2)))
    email_from = my_user
    recipient_list = ['rikhavdedhia.2016@gmail.com']#,'d.parikh511@gmail.com','mit.sheth00796@gmail.com','vrajshah180@gmail.com']
    send_mail( subject, message_renter, email_from, RenterEmail,connection=new_conn)
    send_mail( subject, message_owner, email_from, OwnerEmail,connection=new_conn)

class OldBookingDetails(generic.DetailView):
        model = models.Booking
        template_name = "Booking/oldBooking_Detail.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            try:
                feedback = rmodels.VehicleFeedback.objects.get(booking__pk=self.kwargs.get('pk'))
                context["feedBackGiven"] = False
                context['feedback'] = feedback
            except:
                context["feedBackGiven"] = True
            return context

class OwnerBookingDetails(generic.DetailView):
        model = models.Booking
        template_name = "Booking/OwnerBooking_Detail.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            try:
                feedback = omodels.RenterFeedback.objects.get(booking__pk=self.kwargs.get('pk'))
                context["feedBackGiven"] = False
                context['feedback'] = feedback
            except:
                context["feedBackGiven"] = True
            return context
