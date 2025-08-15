from django.shortcuts import render

from django.shortcuts import render
# You might need to import your Post model later, but not for this basic view
# from .models import Post

def home_view(request):
    """
    Renders the blog homepage template.
    This function handles requests to the blog's root URL.
    """
    # The render() function takes:
    # 1. The request object
    # 2. The template path (Django will look in blog/templates/blog/index.html due to APP_DIRS=True)
    # 3. A dictionary of context variables (optional, but good practice to include if passing data)
    return render(request, 'blog/index.html', {})
# Create your views here.
