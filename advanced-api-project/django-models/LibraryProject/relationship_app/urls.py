from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('books/', list_books(), name='books'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('login/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/', views.register, name='register'),
    path('view/admin/', views.admin_view, name='admin_view'),
    # path('view/admin/', admin_view.AdminView.as_view(), name='admin_view'),
    path('view/librarian/', views.librarian_view, name='librarian_view'),
    path('view/member/<int:id>', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),

]