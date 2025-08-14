"""
URL configuration for advanced_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from api.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
# from .views import BookListCreateView, BookDetailUpdateDeleteView



from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

#     path('admin/', admin.site.urls),path('api', include('api.urls')),  # Include the API URLs
#     path('books/', BookListView.as_view(), name='book-list'),
#     path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
#     path('books/create/', BookCreateView.as_view(), name='book-create'),
#     path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
#     path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),


# urlpatterns = [
#     path('api/', include('api.urls')),  # Include the API URLs
#     # path('admin/', admin.site.urls),
# ]

        
#     path('books/', BookListCreateView.as_view(), name='book_list_create '),
#     path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book_detail_update_delete'),
    

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
