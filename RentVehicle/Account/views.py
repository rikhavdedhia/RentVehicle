from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy #If some1 loggedin or logged out, where should the user go
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponseRedirect
User = get_user_model()
from . import models

# Create your views here.
# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

def RenterSignUp(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(data = request.POST)
        renter_form = forms.RenterForm(data = request.POST)
        if user_form.is_valid() and renter_form.is_valid():
            user = user_form.save()
            renter = renter_form.save(commit=False)
            renter.user = user
            renter.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
    else:
        user_form = forms.UserCreateForm
        renter_form = forms.RenterForm
    return render(request, 'accounts/rentersignup.html',{'user_form' : user_form, 'renter_form' : renter_form})

def OwnerSignUp(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(data = request.POST)
        owner_form = forms.OwnerForm(data = request.POST)
        if user_form.is_valid() and owner_form.is_valid():
            user = user_form.save()
            owner = owner_form.save(commit=False)
            owner.user = user
            owner.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
    else:
        user_form = forms.UserCreateForm
        owner_form = forms.OwnerForm
    return render(request, 'accounts/ownersignup.html',{'user_form' : user_form, 'owner_form' : owner_form})

def RenterLogin(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                if models.Renter.objects.filter(user = user):
                    login(request, user)
                    return redirect(reverse('Renter:AvailableVehicles'))
                else:
                    error = "User does not have a Renter account"
            else:
                error = "User is not active"
        else:
            error = "Invalid Login Details Supplied!!"
    return render(request, 'accounts/renterlogin.html',{'error' : error})

def OwnerLogin(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                if models.Owner.objects.filter(user = user):
                    login(request, user)
                    return redirect(reverse('Owner:OwnerVehicles'))
                else:
                    error = "User does not have a Owner account"
            else:
                error = "User is not active"
        else:
            error = "Invalid Login Details Supplied!!"
    return render(request, 'accounts/ownerlogin.html', {'error' : error})
