from django.conf.urls import url
from .views import ImageAPI 

urlpatterns = [
    url(r'^predict/$', ImageAPI.as_view()),
]
