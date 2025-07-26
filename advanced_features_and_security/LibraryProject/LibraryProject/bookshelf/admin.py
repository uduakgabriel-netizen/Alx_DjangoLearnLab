# from django.contrib import admin

# # Register your models here.
# # <<<<<<< HEAD
# from django.contrib import admin
# from .models import Book

# # Register Book model with customization.

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'publication_year')  # Display these fields in admin list
#     list_filter = ('author', 'publication_year')            # Add filters by author and year
#     search_fields = ('title', 'author')  
#     # Enable search by title and author
# #    ordering = ('-publication_year',)                      # Order by publication year descending
# # =======
# # >>>>>>> 898469f4baf57a4ab64c4ccc59cc8c2afc999553

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
