# blog/urls.py
from django.urls import path
from . import views
from .views import  (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView,
    CommentListView,  
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    # path('login/', views.login_view, name='login'),  # Assuming you have a login view
    path('', PostListView.as_view(), name='home'),  # Home page with list of posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view for a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  #
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    
     # New Comment URLs
    # URL for creating a new comment for a specific post.
    # <int:post_pk> captures the primary key of the post the comment belongs to.
    path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:post_pk>/comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    # URL for editing an existing comment.
    # <int:pk> captures the primary key of the comment itself.
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    # URL for deleting an existing comment.
    # intpk> captures the primary key of the comment itself.
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comments/<int:pk>/detail/', CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
]