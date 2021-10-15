
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from api.custom_renderers import JPEGRenderer
from rest_framework.views import APIView

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from api.models import ImageData
from .serializers import FileSerializer

from .modelAI import predict_image

class ImageAPIView (generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]
    def get(self, request, *args, **kwargs):
        queryset = ImageData.objects.last()
        queryset.imagePredict.name = predict_image(queryset.imageOrigin.path, queryset.imageBackground.path)
        queryset.save()
        data = queryset.imagePredict
        return Response(data, content_type='image/jpg')

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)