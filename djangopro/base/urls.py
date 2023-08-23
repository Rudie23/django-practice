
from django.urls import path
from djangopro.base.views import home
from djangopro.base import views

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', views.login_user, name='login')
]
