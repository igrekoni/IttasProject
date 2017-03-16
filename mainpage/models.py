from django.db import models


# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=160)
    description = models.CharField(max_length=220)
    content = models.TextField()
