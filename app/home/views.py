from django.shortcuts import render
import requests
from django.http import HttpResponse
from books.serializers import BookSerializer
# Create your views here.

def index(request):
    response = requests.get('http://localhost:8000/api/book-list/')
    data = response.json()
    return render(request, 'index.html', {'books': data})
