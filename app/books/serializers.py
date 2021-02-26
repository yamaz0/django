from rest_framework import serializers
from .models import Book, UserBook
from users.serializers import UserSerializer, User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'author', 'rate']


class UserBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()
    class Meta:
        model = UserBook
        fields = ['id', 'user', 'book', 'userRate', 'read']


    def create(self, validated_data):
        data = validated_data.pop('user')
        username = data.pop('username')
        user = User.objects.all().get(username=username)
        data = validated_data.pop('book')
        title = data['title']
        book = Book.objects.get(title=title)
        userBook = UserBook.objects.create(book=book, user=user, **validated_data)
        return userBook

    def update(self, instance, validated_data):
        instance.user = instance.user
        instance.book = instance.book
        instance.userRate = validated_data.get('userRate')
        instance.read = validated_data.get('read')
        instance.save()
        return instance
