from rest_framework import serializers
from .models import ImageData

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = ImageData
    fields = ('imageOrigin','imageBackground')