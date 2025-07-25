# relationship_app/urls.py

# relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app' # URL namespace for this app

urlpatterns = [
    # URL for the function-based view (e.g., /relationship/books/)
    path('books/', views.list_books, name='list_books'),

    # URL for the class-based view (e.g., /relationship/library/1/)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
