from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),
    path('register/', views.create_auth, name = "create_auth"),
    path('change-password/', views.changePassword, name = "changePassword"),
    path('book-list/', views.bookList, name = "book-list"),
    path('book-search/<str:searchTitle>', views.bookSearch, name = "book-list"),
    path('book-detail/<str:pk>', views.bookDetail, name = "book-detail"),
    path('book-create/', views.bookCreate, name = "book-create"),
    path('book-update/<str:pk>', views.bookUpdate, name = "book-update"),
    path('book-delete/<str:pk>', views.bookDelete, name = "book-delete"),

    # path('author-list/', views.authorList, name = "author-list"),
    # path('author-detail/<str:pk>', views.authorDetail, name = "author-detail"),
    # path('author-create/', views.authorCreate, name = "author-create"),
    # path('author-update/<str:pk>', views.authorUpdate, name = "author-update"),
    # path('author-delete/<str:pk>', views.authorDelete, name = "author-delete"),

    path('userBook-list/', views.userBookList, name = "userBook-list"),
    path('userBook-detail/<str:pk>', views.userBookDetail, name = "userBook-detail"),
    path('userBook-create/', views.userBookCreate, name = "userBook-create"),
    path('userBook-update/<str:pk>', views.userBookUpdate, name = "userBook-update"),
    path('userBook-delete/<str:pk>', views.userBookDelete, name = "userBook-delete"),
]