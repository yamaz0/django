from django import forms
from books.models import Book, UserBook,genreEnum
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'author']

class BookForm(forms.ModelForm):
    # title = forms.CharField(label='title', max_length=100)
    # genre = forms.ChoiceField(label='genre',choices= genreEnum.choices)
    # author = forms.ChoiceField(label='author',choices = ['{}'.format(author) for author in Author.objects.all()])
    # rate = forms.IntegerField(label='rate')
    id = forms.IntegerField(label='id', widget=forms.HiddenInput())

    def __init__(self, book, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.initial['id'] = book['id']
        self.initial['title'] = book['title']
        self.initial['genre'] = book['genre']
        self.initial['author'] = book['author']
        # self.title = forms.CharField(label='title', max_length=100, initial=book['title'])
        # self.genre = forms.CharField(label='genre', max_length=100, initial=book['genre'])
        # self.author = forms.CharField(label='author', max_length=100, initial=book['author'])
        # self.rate = forms.IntegerField(label='rate', initial=book['rate'])
        # self.fields['author'] = forms.ChoiceField(choices=tuple([(name, name) for name in book]))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get("title")
    #     genre = cleaned_data.get("genre")
    #     author = cleaned_data.get("author")
    #     rate = cleaned_data.get("rate")
    #     return self.cleaned_data

    class Meta:
        model = Book
        fields = ['title', 'genre', 'author', 'rate']
