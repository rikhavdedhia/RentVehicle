from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from dropdowndb import models
from Account import models as amodels
from . import forms
from Vehicle.models import Filter

def HomePage(request):
    form = forms.CreateFilter()
    error = ''
    if request.method == "POST":
        filterform = forms.CreateFilter(data = request.POST)
        if filterform.is_valid():
            filter = filterform.save(commit=False)
            if models.ZipCode.objects.filter(zipcode = filter.zipcode):
                old_filter = Filter.objects.filter(user=None)
                if old_filter:
                    old_filter.update(zipcode=filter.zipcode)
                else:
                    filter.save()
                return HttpResponseRedirect(reverse('Vehicle:all'))
            else:
                error = "Invalid ZipCode"
    if request.user.is_anonymous:
        return render (request,'index.html',context = {'error' : error, 'form' : form})
    elif amodels.Renter.objects.filter(user = request.user).count():
        return HttpResponseRedirect(reverse('Renter:AvailableVehicles'))
    elif amodels.Owner.objects.filter(user = request.user).count():
        return HttpResponseRedirect(reverse('Owner:OwnerVehicles'))

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def SignUp(request):
    return render(request, 'signup.html')

def LogIn(request):
    return render(request, 'login.html')
