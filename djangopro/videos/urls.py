from django.urls import path

from djangopro.videos.views import video, index

app_name = 'videos'

urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('index', index, name='index'),
]
