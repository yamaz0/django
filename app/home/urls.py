from django.urls import path, include
from .views import index, modify, create, register
from django.contrib.auth.views import LoginView, LogoutView
htmlpatterns = [
    path('', index, name="index"),
    path('modifyBook.html', modify, name="modify"),
    path('register.html', register, name="register"),
    path('createBook.html', create, name="create"),
    path('login.html', LoginView.as_view(
            template_name='login.html'
        ), name="login"),
    path('logout.html',
         LogoutView.as_view(),
         name="logout"),
]
