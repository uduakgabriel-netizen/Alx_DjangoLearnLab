from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import post,Comment
from accounts.serializers import PostSerializer, CommentSerializer
# from accounts.permissions import IsAuthorOrReadOnly # Our custom permission

class PostViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Post instances.
    Provides 'list', 'create', 'retrieve', 'update', 'partial_update', and 'destroy' actions.
    """
    queryset = post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    # IsAuthenticatedOrReadOnly: Allows unauthenticated users to read, but only authenticated users to write.
    # IsAuthorOrReadOnly: Further restricts write access to only the author of the object.

    def perform_create(self, serializer):
        """
        When creating a new post, automatically set the author to the currently authenticated user.
        """
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        """
        Custom action to retrieve all comments for a specific post.
        Accessible at /posts/{pk}/comments/
        """
        post = self.get_object() # Retrieves the specific post based on the pk
        comments = post.comments.all() # Accesses related comments via the 'related_name'
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Comment instances.
    Provides 'list', 'create', 'retrieve', 'update', 'partial_update', and 'destroy' actions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    # Apply the same permission logic: read-only for anyone, write for authenticated,
    # and object-level write for the author.

    def perform_create(self, serializer):
        """
        When creating a new comment, automatically set the author to the currently authenticated user.
        If a 'post_id' is provided in the URL (for nested routes), link the comment to that post.
        """
        # This assumes that if we're using a nested route like /posts/{post_pk}/comments/,
        # the 'post_pk' will be available in self.kwargs.
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            post = get_object_or_404(Post, pk=post_pk)
            serializer.save(author=self.request.user, post=post)
        else:
            # If not nested, expect the 'post' ID to be in the request data
            # and rely on serializer validation to ensure it's provided.
            serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            return queryset.filter(post__pk=post_pk)
        return queryset


