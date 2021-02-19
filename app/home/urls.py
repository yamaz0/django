from django.urls import path, include
from .views import index

htmlpatterns = [
    path('', index, name="index"),
]
