# # relationship_app/urls.py

# from django.urls import path
# from . import views

# app_name = 'relationship_app' # URL namespace for this app

# urlpatterns = [
#     # URL for the function-based view (e.g., /relationship/books/)
#     path('books/', views.list_books, name='list_books'),

#     # URL for the class-based view (e.g., /relationship/library/1/)
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
# ]
from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
     path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]