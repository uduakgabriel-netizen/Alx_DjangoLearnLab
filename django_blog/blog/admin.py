# from django.contrib import admin

# Register your models here.
# blog/admin.py
from django.contrib import admin
from .models import Profile # Importing Profile from blog.models

admin.site.register(Profile)