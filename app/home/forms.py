from django import forms
from books.models import Book, Author, UserBook
import datetime


class BookForm(forms.ModelForm):
    author = forms.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = ['title', 'genre', 'author', 'rate']
