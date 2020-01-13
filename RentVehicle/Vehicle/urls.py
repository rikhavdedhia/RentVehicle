from django.urls import path
from . import views

app_name='Vehicle'

urlpatterns = [
    path('', views.VehicleList.as_view(), name="all"),
    path("VehicleDetails/<VehicleRegistrationNumber>/<int:pk>",views.VehicleDetails.as_view(), name = "VehicleDetails"),
    #path('add/', views.CreateVehicle.as_view(), name='addVehicle')
    #path("new/", views.CreateVehicle.as_view(), name="create"),
    #path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    #path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    #path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
]
