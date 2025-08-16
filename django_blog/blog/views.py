# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Profile # Importing Profile from blog.models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from.forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm, PostForm
from .models import Profile,Post, Comment
from django.urls import reverse, reverse_lazy

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'blog/profile.html', context) # Template path adjusted



# implementing CRUD operations for blog posts


# --- New Blog Post CRUD Views ---

# List all blog posts
class PostListView(ListView):
    model = Post # Specify the model to display
    template_name = 'blog/home.html' # <app>/<post_list.html (default)
                                    
    context_object_name = 'posts' # Name of the queryset variable in the template
    ordering = ['-date_posted'] # Order posts from newest to oldest
    paginate_by = 5 # Display 5 posts per page
    

# Display a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' # Default: <app>/<model>_detail.html
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all comments related to the current post, ordered by creation time
        context['comments'] = self.object.comments.all()
        # Add a blank CommentForm instance to the context for new comments
        context['comment_form'] = CommentForm()
        return context

# Create a new blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm # Use our custom PostForm
    template_name = 'blog/post_form.html' # Default: <app>/<model>_form.html

    def form_valid(self, form):
        # Set the author of the post to the currently logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form) # Call the parent method to save the form

# Update an existing blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Ensure only the author can update their post
        post = self.get_object()
        return self.request.user == post.author

# Delete a blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html' # Custom template for confirmation
    success_url = '/' # Redirect to home page after successful deletion

    def test_func(self):
        # Ensure only the author can delete their post
        post = self.get_object()
        return self.request.user == post.author


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # We don't need a separate template for the form, as it's embedded in post_detail.html
    # This template_name is effectively a fallback, but not directly used for the primary flow.
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Automatically set the author of the comment to the currently logged-in user
        form.instance.author = self.request.user
        
        # Get the 'post_pk' from the URL parameters (defined in urls.py)
        post_pk = self.kwargs.get('post_pk')
        # Fetch the Post object based on the post_pk, or raise a 404 if not found
        form.instance.post = get_object_or_404(Post, pk=post_pk)
        
        # Display a success message to the user
        messages.success(self.request, 'Your comment has been posted!')
        # Call the parent class's form_valid method to save the form instance
        return super().form_valid(form)

    # After a successful comment creation, redirect back to the post's detail page
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs.get('post_pk')})
    
    
    class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Comment
        form_class = CommentForm
        template_name = 'blog/comment_form.html' # Reusing the form template

    def form_valid(self, form):
        # Display a success message after updating
        messages.success(self.request, 'Your comment has been updated!')
        # Call the parent class's form_valid method to save the form instance
        return super().form_valid(form)

    def test_func(self):
        # Get the comment object that is currently being updated
        comment = self.get_object()
        # Return True if the logged-in user is the author of the comment, otherwise False
        return self.request.user == comment.author

    def get_success_url(self):
        # After a successful comment update, redirect back to the associated post's detail page
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html' # Separate template for confirmation

    def test_func(self):
        # Get the comment object that is currently being deleted
        comment = self.get_object()
        # Return True if the logged-in user is the author of the comment, otherwise False
        return self.request.user == comment.author

    def get_success_url(self):
        # After a successful comment deletion, redirect back to the associated post's detail page
        messages.success(self.request, 'Your comment has been deleted!')
        # Using reverse_lazy because the URL might not be available until the project's URLconf is fully loaded
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html' # Separate template for confirmation

    def test_func(self):
        # Get the comment object that is currently being deleted
        comment = self.get_object()
        # Return True if the logged-in user is the author of the comment, otherwise False
        return self.request.user == comment.author

    def get_success_url(self):
        # After a successful comment deletion, redirect back to the associated post's detail page
        messages.success(self.request, 'Your comment has been deleted!')
        # Using reverse_lazy because the URL might not be available until the project's URLconf is fully loaded
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html' # Separate template for confirmation

    def test_func(self):
        # Get the comment object that is currently being deleted
        comment = self.get_object()
        # Return True if the logged-in user is the author of the comment, otherwise False
        return self.request.user == comment.author

    def get_success_url(self):
        # After a successful comment deletion, redirect back to the associated post's detail page
        messages.success(self.request, 'Your comment has been deleted!')
        # Using reverse_lazy because the URL might not be available until the project's URLconf is fully loaded
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})



class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # Use the same template as for creation

    def form_valid(self, form):
        # Set the user of the comment before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Ensure only the owner can update the comment
        comment = self.get_object()
        return self.request.user == comment.user

    def get_success_url(self):
        # Redirect to the post detail page after a successful update
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # Use the same template as for creation

    def form_valid(self, form):
        # Set the user of the comment before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Ensure only the owner can update the comment
        comment = self.get_object()
        return self.request.user == comment.user

    def get_success_url(self):
        # Redirect to the post detail page after a successful update
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})
    
class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        # This assumes you want to filter comments by post, 
        # so it expects a 'pk' in the URL kwargs
        post_pk = self.kwargs.get('pk')
        return Comment.objects.filter(post__pk=post_pk).order_by('-date_posted')