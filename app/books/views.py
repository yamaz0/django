from django.views.generic import ListView

from .models import Book
from .models import UserBook

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class BookcaseListView(ListView):
    model = UserBook
    template_name = 'bookcase_list.html'