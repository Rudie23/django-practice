# from typing import List
#
# from django.shortcuts import get_object_or_404
#
# from djangopro.videos.models import Video
#
#
# def list_videos() -> List:
#     # Return a list arraigned by the time of creation
#
#     return list(Video.objects.order_by('creation').all())
#
#
# def get_video_by_slug(slug):
#     # Getting video from database
#
#     video = get_object_or_404(Video, slug=slug)
#     return video
