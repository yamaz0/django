from rest_framework import serializers
from .models import Book, UserBook
from users.serializers import UserSerializer, User
# from .models import Book, UserBook, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','genre','author','rate']



class UserBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()
    class Meta:
        model = UserBook
        fields = ['user','book','userRate','read']

        # def to_representation(self, instance):
        #     representation = super(UserBookSerializer, self).to_representation(instance)
        #     representation['book'] = BookSerializer(instance.objects.all(), many=False).data
        #     return representation

    def create(self, validated_data):

        data = validated_data.pop('user')
        print(data)
        username = data.pop('username')
        user = User.objects.all().get(username=username)
        print("user")
        print(user)
        print("user")
        data = validated_data.pop('book')
        print(data)
        title = data['title']
        book = Book.objects.get(title=title)

        userBook = UserBook.objects.create(book=book, user=user, **validated_data)

        return userBook
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
