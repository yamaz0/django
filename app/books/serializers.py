from rest_framework import serializers
from .models import Book, UserBook, Author

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Book
        fields = ['id','title','genre','author','rate']


class UserBookSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.StringRelatedField(many=False)
    class Meta:
        model = UserBook
        fields = ['book','userRate','read']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['firstName', 'lastName']
