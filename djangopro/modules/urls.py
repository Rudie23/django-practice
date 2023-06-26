from django.urls import path

from djangopro.modules.views import detail, lesson, index

app_name = 'modules'

urlpatterns = [
    path('<slug:slug>', detail, name='detail'),
    path('lesson/<slug:slug>', lesson, name='lesson'),
    path('', index, name='index')

]
