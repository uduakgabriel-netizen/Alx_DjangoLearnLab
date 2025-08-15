from django.db import models

# Create your models here okay
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"      


# Get all books

# Get all books
# books = book.objects.all()

# Display them
# for book in books:
    # print(book.title, book.author, book.publication_year)
