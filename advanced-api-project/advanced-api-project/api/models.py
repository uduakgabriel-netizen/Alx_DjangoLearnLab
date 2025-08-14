from django.db import models
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer

# this is my models.py file for the advanced API project


class Author(models.Model):
    name = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
        
    