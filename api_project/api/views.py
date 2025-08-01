# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer



# class BookList(generics.ListAPIView):
#     """
#     API view to list all books.
#     """
#     # The queryset specifies the collection of model instances this view will operate on.
#     # Here, we fetch all Book objects from the database.
#     queryset = Book.objects.all()

#     serializer_class = BookSerializer

# api/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed, created, edited, or deleted.
    """
    
    queryset = Book.objects.all()
    
    
    serializer_class = BookSerializer


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)