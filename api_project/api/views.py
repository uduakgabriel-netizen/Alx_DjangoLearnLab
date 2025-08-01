from rest_framework import generics
from .models import Book
from .serializers import BookSerializer



class BookList(generics.ListAPIView):
    """
    API view to list all books.
    """
    # The queryset specifies the collection of model instances this view will operate on.
    # Here, we fetch all Book objects from the database.
    queryset = Book.objects.all()

    serializer_class = BookSerializer
