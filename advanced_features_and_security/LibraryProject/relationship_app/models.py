from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from bookshelf.models import CustomUser

# Create your models here.

# class UserManager(BaseUserManager):
#     # method to handle user creation
#     def create_user(self, username, first_name, last_name, email, password=None):
#         if not username:
#             raise ValueError('Username is required')
        
#         if not email:
#             raise ValueError('Email is required')
        
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name
#         )

#         user.set_password(password)
#         # save to default database configured
#         user.save(using=self._db)
#         return user

#     # method to handle superuser creation
#     def create_superuser(self, username, first_name, last_name, email, password=None):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             password=password
#         )

#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superadmin = True

#         # save to default database configured
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField()
#     profile_photo = models.ImageField(upload_to='gallery')

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_add_book', 'Can Add Book'),
            ('can_change_book', 'Can Change Book')
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    labrary = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
    