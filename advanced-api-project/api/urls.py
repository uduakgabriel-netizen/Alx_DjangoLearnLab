from django.contrib import admin
from django.urls import path
from api.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .views import BookListCreateView, BookDetailUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),
]


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book_list_create '),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),
]
 