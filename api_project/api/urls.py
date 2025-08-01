# from django.urls import path
# from .views import BookList

# # urlpatterns is a list of URL patterns that Django will use
# # to route incoming requests.
# urlpatterns = [
#     path('', BookList.as_view(), name='book-list'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router = DefaultRouter()


router.register(r'books', BookViewSet)


urlpatterns = [
   
    path('', include(router.urls)),
]
