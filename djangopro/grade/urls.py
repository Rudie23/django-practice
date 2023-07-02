from django.urls import path
from djangopro.grade import views

app_name = 'grade'

urlpatterns = [
    path('', views.index, name='index'),

]
