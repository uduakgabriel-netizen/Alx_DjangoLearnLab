from django.urls import path
from . import views # Import the views module from the current directory

# Define app_name for namespacing. This helps prevent URL conflicts if you have
# multiple apps with similar URL names (e.g., 'detail').
app_name = 'blog'

urlpatterns = [
    # path('', ...): This maps the empty path (e.g., /blog/) to the home_view.
    # views.home_view: The function in blog/views.py to call.
    # name='home': A unique name for this URL pattern, useful for reverse URL lookups.
    path('', views.home_view, name='home'),
]
