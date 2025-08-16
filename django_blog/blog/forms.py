# blog/forms.py
from .models import Comment  # Importing Comment model from blog.models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, Post # Now importing Profile from blog.models

# Custom form for user registration to include email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)


# Form for updating user details (username, email, first/last name)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# Form for updating profile details (image, bio)
# This requires the Profile model to be defined in blog/models.py
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
        
# New PostForm for creating and updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post  # Link this form to the Post model
#         fields = ['title', 'content']

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'Comment by {self.author.username} on {self.post.title}'



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Only include the 'content' field for user input.
        # 'post', 'author', 'created_at', 'updated_at' will be handled automatically by the view/model.
        fields = ['content']
        # Optional: Add widgets for better control over form field appearance.
        # Here, we use a Textarea with specified rows and a placeholder.
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }


# meta = {
#     'model': Comment,
# }