from rest_framework import generics
from .models import Book
from .serializer import BookSerializer

class BookList(generics.ListAPIView):
    
    """""
    API view to retrieve list of books
    
    """""
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

