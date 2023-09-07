from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from djangopro.base.forms import UserForm


# Create your views here.


def home(request):
    return render(request, 'base/home.html', {})


def register_user(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Message of success
            messages.success(request, "Your account has been registered.")
            user = form.save()
            # Whatever the data submitted with a form, once it has been successfully validated by calling is_valid()
            # (and is_valid() has returned True), the validated form data will be in the form.cleaned_data
            # dictionary. This data will have been nicely converted into Python types for you. In the contact form
            # example above, cc_myself will be a boolean value. Likewise, fields such as IntegerField and FloatField
            # convert values to a Python int and float respectively.

            login(request, user)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('base:home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            return HttpResponseRedirect(reverse('modules:index'))
        else:
            messages.error(request, "There was an error logging in, try again...")
            # Return an 'invalid login' error message.
            return HttpResponseRedirect(reverse('base:login'))
    return render(request, 'registration/login.html', {})
