from rest_framework import serializers
from .models import Book, UserBook
# from .models import Book, UserBook, Author

class UserBookSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(many=False)
    class Meta:
        model = UserBook
        fields = ['book','userRate','read']

        # def create(self, validated_data):
        #     books_data = validated_data.pop('books')
        #     book = UserBook.objects.create(**validated_data)
        #     for track_data in books_data:
        #         Book.objects.create(book=book, **books_data)
        #     return book
        #
        # def update(self, instance, validated_data):
        #     book = validated_data.get('book')
        #
        #     instance.book.title = book.get('title')
        #     instance.book.genre = book.get('genre')
        #     instance.book.author = book.get('author')
        #     instance.book.rate = book.get('rate')
        #     instance.book.save()
        #     return instance

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','genre','author','rate']
