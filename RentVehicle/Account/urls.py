from django.urls import path
from django.contrib.auth import views as auth_views#For Login and Logout views
#We need not create class for them
from . import views

app_name = 'Account'

urlpatterns = [
    #path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("RenterSignUp/", views.RenterSignUp, name="RenterSignUp"),
    path("OwnerSignUp/", views.OwnerSignUp, name="OwnerSignUp"),
    path("RenterLogIn/", views.RenterLogin, name="RenterLogIn"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("OwnerLogIn/", views.OwnerLogin, name="OwnerLogIn"),
]
