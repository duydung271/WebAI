from django.urls import path
from django.conf.urls import url, include
from .views import FileView, ImageAPIView

urlpatterns = [
    path('image_predict/', ImageAPIView.as_view()),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
]
