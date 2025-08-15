# blog/urls.py
from django.urls import path
from . import views
from .views import  (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    # path('login/', views.login_view, name='login'),  # Assuming you have a login view
    path('', PostListViews.as_views(), name='home'),  # Home page with list of posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view for a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  #
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    
     # New Comment URLs
    # URL for creating a new comment for a specific post.
    # <int:post_pk> captures the primary key of the post the comment belongs to.
    path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    # URL for editing an existing comment.
    # <int:pk> captures the primary key of the comment itself.
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    # URL for deleting an existing comment.
    # <int:pk> captures the primary key of the comment itself.
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]