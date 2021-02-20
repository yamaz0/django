from django.shortcuts import render
import requests
from .forms import BookForm
from django.http import HttpResponse
from books.serializers import BookSerializer
# Create your views here.

def index(request):
    response = requests.get('http://localhost:8000/api/book-list/')
    data = response.json()
    return render(request, 'index.html', {'books': data})

def modify(request):
    id = request.GET.get('pk', '')
    response = requests.get('http://localhost:8000/api/book-detail/{0}'.format(id))
    data = response.json()
    form = BookForm(data)
    return render(request, 'modifyBook.html', {'form': form})


    # interview = Interview.objects.get(pk=interview_pk)
    # all_rounds = interview.round_set.order_by('created_at')
    # all_round_names = [rnd.name for rnd in all_rounds]
    # form = forms.AddRatingForRound(all_round_names)
    # return render(request, 'add_rating.html', {'form': form, 'interview': interview, 'rounds': all_rounds})