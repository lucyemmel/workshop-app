from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()