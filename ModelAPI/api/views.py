
# Create your views here.
import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from .modelAI import image_decode, image_encode, predict_image


class ImageSerializer(serializers.Serializer):
  origin = serializers.CharField(max_length=10000000)
  background = serializers.CharField(max_length=10000000)

class PredictSerializer(serializers.Serializer):
  predict = serializers.CharField(max_length=10000000)    

class ImageAPI(APIView):

  def post(self, request):
    serializer = ImageSerializer(data = request.data)
    if serializer.is_valid():
      img_origin = image_decode(serializer.validated_data['origin'], "origin.png")
      img_background = image_decode(serializer.validated_data['background'], "background.png")
      img_predict = predict_image(os.path.join(settings.MEDIA_ROOT, img_origin),os.path.join(settings.MEDIA_ROOT, img_background))

      base64_image = image_encode(img_predict)
      data = {'predict': base64_image}
      predict_serializer =PredictSerializer(data=data)
      if predict_serializer.is_valid():
        return Response(predict_serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)