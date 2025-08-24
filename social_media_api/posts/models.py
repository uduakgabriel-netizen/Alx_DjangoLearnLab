

from django.db import models
from django.contrib.auth.models import User # Import Django's default User model

class Post(models.Model):
    """
    Represents a social media post made by a user.

    Attributes:
        author (ForeignKey): The user who created the post.
                             When the author is deleted, all their posts are also deleted (CASCADE).
                             'related_name="posts"' allows accessing a user's posts via user.posts.all().
        title (CharField): The title of the post, limited to 255 characters.
        content (TextField): The main body content of the post.
        created_at (DateTimeField): Automatically sets the creation timestamp when the post is first saved.
        updated_at (DateTimeField): Automatically updates the timestamp every time the post is saved.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Orders posts by creation date in descending order by default
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the Post, typically its title.
        """
        return self.title

class Comment(models.Model):
    """
    Represents a comment made on a Post.

    Attributes:
        post (ForeignKey): The post this comment belongs to.
                           When the associated post is deleted, this comment is also deleted (CASCADE).
                           'related_name="comments"' allows accessing a post's comments via post.comments.all().
        author (ForeignKey): The user who made the comment.
                             When the author is deleted, all their comments are also deleted (CASCADE).
                             'related_name="comments"' allows accessing a user's comments via user.comments.all().
        text (TextField): The actual text content of the comment.
        created_at (DateTimeField): Automatically sets the creation timestamp.
        updated_at (DateTimeField): Automatically updates the timestamp upon modification.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Orders comments by creation date in ascending order by default
        ordering = ['created_at']

    def __str__(self):
        """
        Returns a string representation of the Comment, showing the author and the post it's on.
        """
        return f"Comment by {self.author.username} on {self.post.title}"


