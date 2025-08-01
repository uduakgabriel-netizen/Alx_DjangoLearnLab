from django.rest_framework import serializers
from.models import Book  # Assuming you have a Book model defined in models.py

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # or specify the fields you want to include