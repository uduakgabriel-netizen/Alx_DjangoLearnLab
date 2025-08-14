from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from.filters import BookFilter
from rest_framework import generics, filters
from.serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from django.contrib.auth.mixins import UserPassesTestMixin
# from rest_framework import 
# from rest_framework.permissions import IsAuthenticated,IsauthenticatedOrReadOnly, authenticated
# from django.contrib.auth.mixins import UserPassesTestMixin


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'books'
    
class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('book-list')
    
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('book-list')
    
    
class BookCreateView(LoginRequiredMixin, CreateView):
    # This view now requires a logged-in user
    model = Book
    # ... (other attributes)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    # This view now requires a logged-in user
    model = Book
    # ... (other attributes)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    # This view now requires a logged-in user
    model = Book
    # ... (other attributes)
    
    
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'publication_date']
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user # Checks if the book owner matches the current user

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user 
    
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_date']
    
class BookList(generics.ListAPIView):
    """
    API view with advanced filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Use all three backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Custom filterset class for advanced filtering
    filterset_class = BookFilter
    
    # Search and ordering fields
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_date']
    ordering = ['title']
    
    
    
    
# Filtering: We used django-filter to create a declarative FilterSet class (BookFilter) that links to our Book model. This allows us to filter books by publication_year. This is configured in the BookList view using filterset_class.

# Searching: We integrated the SearchFilter into our filter_backends. We then specified the searchable fields, title and author, using the search_fields attribute.

# Ordering: We enabled the OrderingFilter and listed title and publication_date in the ordering_fields attribute, allowing clients to sort results by these fields. We also set a default ordering of title.

# 2. API Usage Examples
# The following examples demonstrate how clients can interact with the API to filter, search, and order the book list.

# Filter by publication year: To retrieve all books published in 2023, use the publication_year query parameter.

# GET /books/?publication_year=2023
# Search by title or author: To find books containing the word "python" in either the title or author, use the search parameter.

# GET /books/?search=python
# Order by publication date (descending): To sort the book list from newest to oldest, use the ordering parameter with a hyphen.

# GET /books/?ordering=-publication_date
# Combine filters: You can combine multiple parameters for more specific results.

# GET /books/?search=dune&publication_year=1965&ordering=title