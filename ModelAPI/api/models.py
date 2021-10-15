from django.db import models

# Create your models here.

class ImageData(models.Model):
    imageOrigin = models.ImageField()
    imageBackground= models.ImageField()
    imagePredict = models.ImageField()