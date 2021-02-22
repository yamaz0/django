from django.shortcuts import render, redirect
from .forms import BookCreateForm, BookForm, RegisterForm
import requests
from books.models import Book
from django.http import HttpResponse
from django.http import JsonResponse
# from books.
# Create your views here.



def index(request):
    return render(request, 'listBook.html')

def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def create(request):
    form = BookCreateForm()
    return render(request, 'createBook.html', {'form': form})

def modify(request):
    id = request.GET.get('pk', '')
    response = requests.get('http://localhost:8000/api/book-detail/{0}'.format(id))
    data = response.json()
    print(data)
    form = BookForm(book=data)
    return render(request, 'modifyBook.html', {'form': form})