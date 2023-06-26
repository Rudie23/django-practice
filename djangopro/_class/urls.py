from django.urls import path
from djangopro._class import views

app_name = '_class'

urlpatterns = [
    path('', views.index, name='index'),

]
