from django.urls import path
from . import views


urlpatterns = [
    path('', views.img, name='img'),
]