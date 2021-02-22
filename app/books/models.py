from django.db import models
#from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
# class Author(models.Model):
#     firstName = models.CharField(max_length=250)
#     lastName = models.CharField(max_length=250)
#
#     def __str__(self):
#         return ("{first_name} {last_name}").format(first_name=self.firstName, last_name=self.lastName)

class genreEnum(models.TextChoices):
    FANTASY = 'Fantasy'
    SCIFI = 'Sci-Fi'
    MYSTERY = 'Mystery'
    THRILLER = 'Thriller'
    ROMANCE = 'Romance'
    WESTERNS = 'Westerns'
    DYSTOPIAN = 'Dystopian'
    CONTEMPORARY = 'Contemporary'
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 250)
    genre = models.CharField(
        max_length=255,
        choices=genreEnum.choices,
        default=genreEnum.FANTASY,
    )
    rate = models.IntegerField(default=0)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length = 250)
    isbn = models.CharField(max_length = 13)

    def __str__(self):
        return self.title


#Ksiazki uzytkownika w biblioteczce
class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    userRate = models.IntegerField(default=0)
    read = models.BooleanField(default=False)

def __str__(self):
    return self.title
