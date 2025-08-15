from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

class CustomUserManager(BaseUserManager):
    # method to handle user creation
    def create_user(self, username, first_name, last_name, email, password=None):
        if not username:
            raise ValueError('Username is required')
        
        if not email:
            raise ValueError('Email is required')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        # save to default database configured
        user.save(using=self._db)
        return user

    # method to handle superuser creation
    def create_superuser(self, username, first_name, last_name, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        # save to default database configured
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='gallery', blank=True, null=True)


class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()

  class Meta:
      permissions = [
          ('can_view', 'Can View'),
          ('can_create', 'Can Create'),
          ('can_edit', 'Can Edit'),
          ('can_delete', 'Can Delete')
      ]
