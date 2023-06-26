from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    begin = models.DateField()
    end = models.DateField()
    students = models.ManyToManyField(get_user_model(), through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)

    # With class Meta, you can restrict a creation of enrollment to once time
    class Meta:
        unique_together = [['user', '_class']]
        ordering = ['_class', 'date']

    def __str__(self):
        return self.user
