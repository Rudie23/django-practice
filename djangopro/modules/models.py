from django.db import models
from ordered_model.models import OrderedModel


# Create your models here.

class Module(OrderedModel):
    title = models.CharField(max_length=64)
    public = models.TextField()
    description = models.TextField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title
