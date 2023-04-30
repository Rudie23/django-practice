
from django.urls import path
from djangopro.base.views import home

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
]
