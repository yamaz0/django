from django import forms
from books.models import Book, Author, UserBook
import datetime


class BookForm(forms.ModelForm):

    def __init__(self, book, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['id','title', 'genre', 'author', 'rate'] = forms.ChoiceField(choices=tuple([(name, name) for name in book]))

    class Meta:
        model = Book
        fields = ['id','title', 'genre', 'author', 'rate']
