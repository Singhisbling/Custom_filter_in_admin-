from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    price2 = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class BD(models.Model):
    pl = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.pl
