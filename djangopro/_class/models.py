from django.db import models


# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    begin = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name
