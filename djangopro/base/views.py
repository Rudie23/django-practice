from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, 'base/home.html', {})


def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            return redirect('modules:index')
        else:
            messages.success(request, "There was an error logging in, try again...")
            # Return an 'invalid login' error message.
            return redirect('login')
    return render(request, 'registration/login.html', {})
