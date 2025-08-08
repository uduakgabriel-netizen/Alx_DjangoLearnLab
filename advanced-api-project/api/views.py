from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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
        return obj.owner == self.request.user # Checks if the book owner matches the current user