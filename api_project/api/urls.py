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
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()


router.register(r'books', BookViewSet)


urlpatterns = [
   
    path('', include(router.urls)),
    
     path('auth/', obtain_auth_token, name='api-token-auth'),
]
