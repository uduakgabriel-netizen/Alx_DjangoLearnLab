from django.urls import path
from .views import BookList

# urlpatterns is a list of URL patterns that Django will use
# to route incoming requests.
urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
]
