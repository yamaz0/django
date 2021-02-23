from django.shortcuts import render, redirect
from .forms import BookCreateForm, BookForm, RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import requests
from books.models import Book
from django.http import HttpResponse
from django.http import JsonResponse
# from books.
# Create your views here.



def index(request):
    return render(request, 'listBook.html')

def map(request):
    return render(request, 'map.html')

def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def changePassword(request):
    # if request.method == 'PUT':
    #     form = PasswordChangeForm(request.user, request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)  # Important!
    #         messages.success(request, 'Your password was successfully updated!')
    #         return redirect('change_password')
    #     else:
    #         messages.error(request, 'Please correct the error below.')
    # else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changePassword.html', {'form': form})

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