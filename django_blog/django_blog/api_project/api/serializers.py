

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It includes all fields from the Book model.
    """
    class Meta:
        
        model = Book
        
        
        fields = '__all__'
