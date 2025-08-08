from django.contrib import admin
from django.urls import path
from api.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .views import BookListCreateView, BookDetailUpdateDeleteView
from django.urls import include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the API URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),
]


# urlpatterns = [
#     path('books/', BookListCreateView.as_view(), name='book_list_create '),
#     path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),
# ]



# from django.urls import path
# from .views import (
#     BookListView,
#     BookDetailView,
#     BookCreateView,
#     BookUpdateView,
#     BookDeleteView,
# )

# urlpatterns = [
#     path('books/', BookListView.as_view(), name='book_list'),
#     path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
#     path('books/new/', BookCreateView.as_view(), name='book_create'),
#     # This is the path for the update view, it requires a primary key.
#     path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
#     # This is the path for the delete view, it also requires a primary key.
#     path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
# ]


# from django.urls import path
# from .views import BookListCreateView, BookDetailUpdateDeleteView

# urlpatterns = [
#     # GET: List all books. POST: Create a new book.
#     path('books/', BookListCreateView.as_view(), name='book_list_create'),
    
#     # GET: Retrieve a book. PUT/PATCH: Update a book. DELETE: Delete a book.
#     path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),
# ]