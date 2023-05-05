from django.shortcuts import render, get_object_or_404

from djangopro.videos.models import Video


# Create your views here.


def index(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'videos/index.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'videos/videos.html', context={'video': video})
