"""RentVehicle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name = 'home'),
    path('SignUp/',views.SignUp, name = 'SignUp'),
    path('LogIn/',views.LogIn, name = 'LogIn'),
    path("accounts/", include("Account.urls", namespace="accounts")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('test/', views.TestPage.as_view(), name = 'test'),
    path('thanks/', views.ThanksPage.as_view(), name = 'thanks'),
    path('vehicle/',include("Vehicle.urls", namespace="vehicles")),
    path("owner/", include("Owner.urls", namespace="owner")),
    path("renter/", include("Renter.urls", namespace="renter")),
    path("booking/", include("Booking.urls", namespace="booking")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
