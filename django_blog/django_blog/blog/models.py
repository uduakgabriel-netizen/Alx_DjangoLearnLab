from django.db import models

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

# Create your models here.

class Post(models.Model):
    """
    Represents a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # ForeignKey to Django's User model:
    # - User: The related model (Django's built-in User).
    # - on_delete=models.CASCADE: If a User is deleted, all their associated
    #   posts will also be deleted. This is a common and appropriate behavior.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the Post object, which is its title.
        This is helpful for displaying the post in the Django admin and other places.
        """
        return self.title

    class Meta:
        """
        Meta options for the Post model.
        - ordering: Specifies the default ordering for querysets.
                    Here, posts will be ordered by 'published_date' in descending order
                    (newest first). The '-' indicates descending order.
        """
        ordering = ['-published_date']
