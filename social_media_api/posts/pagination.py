from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    """
    Custom pagination class to control the number of items per page.
    - page_size: The default number of items per page.
    - page_size_query_param: Allows clients to specify a custom page size using a query parameter.
    - max_page_size: The maximum number of items a client can request per page.
    """
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size' # Allows clients to set page size using ?page_size=X
    max_page_size = 100 # Maximum page size allowed
