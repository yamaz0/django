from rest_framework import serializers
from .models import Book, UserBook
from users.serializers import UserSerializer, User
# from .models import Book, UserBook, Author

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
        # extra_kwargs = {'user': {'required': False},
        #                 'book': {'required': False}
        #                 }
        # def to_representation(self, instance):
        #     representation = super(UserBookSerializer, self).to_representation(instance)
        #     representation['book'] = BookSerializer(instance.objects.all(), many=False).data
        #     return representation

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
        # userdata = validated_data.get('user')
        # title = validated_data.get('title')
        # bookData = validated_data.get('book')
        # print(validated_data)
        # book = Book.objects.filter(title=bookData['title']).first()
        # print(book)
        # user = User.objects.get(username=userdata['username'])
        # instance.user = user
        # instance.book = book
        instance.user = instance.user
        instance.book = instance.book
        instance.userRate = validated_data.get('userRate')
        instance.read = validated_data.get('read')
        instance.save()
        return instance
