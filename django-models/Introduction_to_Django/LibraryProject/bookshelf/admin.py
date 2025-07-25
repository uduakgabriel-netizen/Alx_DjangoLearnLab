from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Register Book model with customization.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in admin list
    list_filter = ('author', 'publication_year')            # Add filters by author and year
    search_fields = ('title', 'author')  
    # Enable search by title and author
#    ordering = ('-publication_year',)                      # Order by publication year descending