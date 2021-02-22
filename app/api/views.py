from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from books.serializers import BookSerializer, UserBookSerializer
from books.models import Book, UserBook
from users.serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data)
    else:
        return Response(serialized._errors)

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'Books list':'/book-list/',
        'Books list':'/book-list/',
        'Book detail':'/book-detail/<str:pk>/',
        'Book create':'/book-create/',
        'Book update':'/book-update/<str:pk>/',
        'Book delete':'/book-delete/<str:pk>/',

        # 'Author list':'/author-list/',
        # 'Author detail':'/author-detail/<str:pk>/',
        # 'Author create':'/author-create/',
        # 'Author update':'/author-update/<str:pk>/',
        # 'Author delete':'/author-delete/<str:pk>/',

        'UserBook list':'/userBook-list/',
        'UserBook detail':'/userBook-detail/<str:pk>/',
        'UserBook create':'/userBook-create/',
        'UserBook update':'/userBook-update/<str:pk>/',
        'UserBook delete':'/userBook-delete/<str:pk>/',
    }
    return Response(api_urls)


#Book
@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def bookDetail(request,pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many = False)
    return Response(serializer.data)

@api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def bookCreate(request):
    serializer = BookSerializer(data = request.data)
    print('aa')
    if serializer.is_valid():
        print('bbb')
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def bookUpdate(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=books, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def bookDelete(request, pk):
    books = Book.objects.get(id=pk)
    books.delete()
    return Response('Item succsesfully delete!')

#Author
# @api_view(['GET'])
# def authorList(request):
#     author = Author.objects.all()
#     serializer = AuthorSerializer(author,many = True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def authorDetail(request,pk):
#     author = Author.objects.get(id=pk)
#     serializer = AuthorSerializer(author, many = False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def authorCreate(request):
#     serializer = AuthorSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def authorUpdate(request, pk):
#     author = Author.objects.get(id=pk)
#     serializer = AuthorSerializer(instance=author, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def authorDelete(request, pk):
#     author = Author.objects.get(id=pk)
#     author.detele()
#     return Response('Item succsesfully delete!')

#UserBook
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userBookList(request):
    user = request.user
    userBook = UserBook.objects.filter(user = user)
    serializer = UserBookSerializer(userBook,many = True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userBookDetail(request,pk):
    user = request.user
    userBook = UserBook.objects.get(id=pk).filter(user = user)
    serializer = UserBookSerializer(userBook, many = False)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userBookCreate(request):
    user = request.user
    serializer = UserBookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userBookUpdate(request, pk):
    user = request.user
    userBook = UserBook.objects.get(id=pk).filter(user = user)
    serializer = UserBookSerializer(instance=userBook, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userBookDelete(request, pk):
    user = request.user
    userBook = UserBook.objects.get(id=pk).filter(user = user)
    userBook.detele()
    return Response('Item succsesfully delete!')


# @api_view(['GET'])
# def useBookList(request,id,pk):
#     userBooks = UserBook.objects.get(id=pk)
#     serializer = UserBookSerializer(userBooks,many = True)
#     return Response(serializer.data)
#