from django.urls import path, include
from .views import index, modify

htmlpatterns = [
    path('', index, name="index"),
    path('modifyBook.html', modify, name="modify"),
]
