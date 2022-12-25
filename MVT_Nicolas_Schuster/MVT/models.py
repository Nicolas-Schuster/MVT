from django.db import models

class Famillia(models.Model):
    name = models.CharField(max_length=50)
    edad = models.IntegerField()
    vive = models.BooleanField()

