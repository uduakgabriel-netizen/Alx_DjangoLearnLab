from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# name: models.CharField(_(""), max_length=50)
# title: modlels.models.CharField(_(""), max_length=50)
# author: models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

# from django.db import models



# Register your models here.

# Autho model.....

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Book model with a foreign key relationship to Author
# Library model with a many-to-many relationship to Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
    

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"