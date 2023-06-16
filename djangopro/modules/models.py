from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


# Create your models here.

class Module(OrderedModel):  # Relation one with N relations (Lesson)
    title = models.CharField(max_length=64)
    public = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:detail', kwargs={'slug': self.slug})


class Lesson(OrderedModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    module = models.ForeignKey('Module', on_delete=models.PROTECT)  # Many
    order_with_respect_to = 'module'
    vimeo_id = models.CharField(max_length=36)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:lesson', kwargs={'slug': self.slug})
