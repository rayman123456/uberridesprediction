from django.db import models

# Create your models here.

class RidesPrediction(models.Model):
    ppw =models.IntegerField()
    pn = models.IntegerField()
    mi = models.IntegerField()
    appm = models.IntegerField()
    res=models.CharField(max_length=20)
