from django.urls import path

from . import views

urlpatterns = [
    path('allBooks/', views.BookListView.as_view(), name = "allBooks"),
    path('bookcase/', views.BookcaseListView.as_view(), name = "bookcase"),
]