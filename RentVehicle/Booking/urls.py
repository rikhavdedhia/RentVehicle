from django.urls import path
from . import views

app_name='Booking'

urlpatterns = [
    path('<VehicleRegistrationNumber>/<int:pk>', views.CreateBooking.as_view(), name="CreateBooking"),
    path('RenterBooking/',views.RenterBookingList.as_view(), name="RenterBookingList"),
    path('OwnerBookingList/',views.OwnerBookingList.as_view(), name="OwnerBookingList"),
    path('<int:pk>', views.RenterBookingDetails.as_view(), name='RenterBookingDetails'),
    path('Owner/Booking/Details<int:pk>', views.OwnerBookingDetails.as_view(), name='OwnerBookingDetails'),
    path('OldBooking/Details/<int:pk>', views.OldBookingDetails.as_view(), name='OldBookingDetails'),
    path('<int:pk>/SelectPayment', views.SelectPayment.as_view(), name='SelectPayment'),
    path('MakePayment/PayByCard/<int:pk>', views.CardPayment.as_view(), name='CardPayment'),
    path('MakePayment/PayByCheck/<int:pk>', views.CheckPayment.as_view(), name='CheckPayment'),
]
