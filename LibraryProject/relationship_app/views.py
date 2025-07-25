# from django.shortcuts import render

# # Create your views here.
# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based View: Lists all books
def list_books(request):
    books = Book.objects.all().order_by('title')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based View: Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library # Specifies the model this view operates on
    template_name = 'relationship_app/library_detail.html' # Path to the template
    context_object_name = 'library' # Name of the object in the template context
