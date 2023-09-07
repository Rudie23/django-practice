from django.db import models
from django.urls import reverse


# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=36)
    slug = models.SlugField(max_length=36)
    vimeo_id = models.CharField(max_length=36)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('videos:video', args=(self.slug,))

    def __repr__(self):
        return f'Vídeo: {self.title}'
