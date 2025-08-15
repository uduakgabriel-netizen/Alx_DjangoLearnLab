# your_app_name/serializers.py
from rest_framework import serializers
# from .models import Book, Author
from datetime import date






class BookSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Book
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        from .models import Author
        model = Author
        fields = ('id', 'name', 'books')

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         from .models import Book  # Move import here
#         model = Book
#         fields = '__all__'

# The BookSerializer handles the serialization and deserialization of the Book model.
# It includes a custom validation method to ensure data integrity.
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         # `fields = '__all__'` serializes every field from the Book model.
#         fields = '__all__'

#     # Custom validation method for the publication_date field.
#     # This method is automatically called by DRF during deserialization (e.g., on POST or PUT).
#     def validate_publication_date(self, value):
#         """
#         Validates that the book's publication date is not in the future.
#         """
#         if value > date.today():
#             raise serializers.ValidationError("Publication date cannot be in the future.")
#         return value

# The AuthorSerializer handles the serialization of the Author model.
# It includes a nested BookSerializer to display an author's related books.
# class AuthorSerializer(serializers.ModelSerializer):
    # This is how the relationship is handled in the serializer:
    # We use a nested serializer (`BookSerializer`) to represent the 'books' related to an Author.
    # The name 'books' must match the `related_name` defined in the ForeignKey of the Book model.
    # `many=True` is required because an Author can have many books.
    # `read_only=True` prevents clients from creating or updating related books through this serializer.
    # books = BookSerializer(many=True, read_only=True)

    # class Meta:
    #     model = Author
    #     # The fields to be serialized include the 'id', 'name', and the nested 'books' list.
    #     fields = ('id', 'name', 'books')