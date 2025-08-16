# blog/models.py
from django.db import models
from django.contrib.auth.models import User# Django's built-in User model
from PIL import Image # Pillow library for image processing
from django.utils import timezone
from taggit.managers import TaggableManager # Import the TaggableManager

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize image to save space and load faster
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)  # Many-to-many relationship with tags

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['-date_posted']  # Order posts by date posted, newest first
        
        
        
        
# Existing Profile model (no change needed here for comments)
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     bio = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img = Image.open(self.image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)

# Existing Post model (no change needed here for comments, but keep it)
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': self.pk})

# New Comment model
class Comment(models.Model):
    # Foreign Key linking to the Post model.
    # If the Post is deleted, all associated comments are also deleted.
    # 'related_name' allows accessing comments from a Post instance (e.g., post.comments.all()).
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    
    # Foreign Key linking to Django’s built-in User model.
    # Indicates the user who wrote the comment. If the User is deleted, their comments are deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # TextField for the comment’s content.
    content = models.TextField()
    
    # DateTimeField that records the time the comment was created.
    # 'auto_now_add=True' automatically sets the field to the current datetime when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    
    # DateTimeField that records the last time the comment was updated.
    # 'auto_now=True' automatically updates the field to the current datetime every time the object is saved.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Default ordering for comments: oldest first.
        ordering = ['created_at']

    def __str__(self):
        # A human-readable representation of the comment object.
        # Shows the author and a snippet of the comment content.
        return f'Comment by {self.author.username} on {self.post.title[:30]}...'

    def get_absolute_url(self):
        # Defines the canonical URL for a Comment instance.
        # Useful for redirects after creating/updating/deleting a comment,
        # usually leading back to the post's detail page.
        return reverse('post-detail', kwargs={'pk': self.post.pk})
    
    class Tag(models.Model):
    """
    Represents a tag that can be associated with blog posts.
    Each tag has a unique name.
    """
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        # Optional: Add a verbose name for the Tag model for better admin display
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        # Optional: Order tags alphabetically by name by default
        ordering = ['name']

    def __str__(self):
        """
        String representation of the Tag, showing its name.
        """
        return self.name

class Post(models.Model):
    """
    Represents a blog post, including title, content, author,
    date posted, and a many-to-many relationship with tags.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Establish a Many-to-Many relationship with the Tag model.
    # 'blank=True' means a post doesn't have to have any tags.
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        # Order posts by date_posted in descending order by default
        ordering = ['-date_posted']

    def __str__(self):
        """
        String representation of the Post, showing its title.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a particular instance of the Post.
        Used by Django's CreateView/UpdateView for redirection.
        """
        return reverse('post-detail', kwargs={'pk': self.pk})
