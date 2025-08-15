# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile # Importing Profile from blog.models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from.forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm, PostForm
from .models import Profile,Post

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
