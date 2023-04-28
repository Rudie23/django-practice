from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
app_name = 'base'


def home(request):
    return HttpResponse("Hello World")
