import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    """
    A FilterSet for the Post model, allowing filtering by title and content.
    - title: Performs a case-insensitive partial match on the post title.
    - content: Performs a case-insensitive partial match on the post content.
    """
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    # Filtering by content, using 'icontains' for case-insensitive containment
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content', 'author'] # You can also filter by author if needed
