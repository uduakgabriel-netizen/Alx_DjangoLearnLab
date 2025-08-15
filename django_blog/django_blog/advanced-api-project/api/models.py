from django.db import models
from rest_framework import generics
# from .serializers import BookSerializer, AuthorSerializer

# this is my models.py file for the advanced API project


class Author(models.Model):
    name = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return self.name
    
    
# class Book(models.Model):
#     title = models.CharField(max_length = 100)
#     publication_year = models.IntegerField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return self.title
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(null=True, blank=True) # Add this line

    def __str__(self):
        return self.title