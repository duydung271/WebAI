
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.homeView, name= 'home'),
    path('home2/',views.homeView2, name= 'home2'),
    path('bg/', views.background, name='background'),
]