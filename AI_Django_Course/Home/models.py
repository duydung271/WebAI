from django.db import models

# Create your models here.
class Holder(models.Model):
    imageOrigin = models.ImageField()
    imageBackground = models.ImageField(default='depqua.jpg')
    imagePredict = models.ImageField()