from django.urls import path
from . import views

app_name='Renter'

urlpatterns = [
    path('', views.ListAvailableVehicles.as_view(), name="AvailableVehicles"),
    path("VehicleDetails/<VehicleRegistrationNumber>/<int:pk>",views.VehicleDetails.as_view(), name = "VehicleDetails"),
    path("RenterFeedback/<VehicleRegistrationNumber>/<int:pk>",views.RenterFeedback.as_view(), name = "RenterFeedback"),
]
