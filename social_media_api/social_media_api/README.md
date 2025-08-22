Social Media API: Project Overview
This document provides a high-level overview of the social_media_api project, a foundational backend for a social media application built using Django and Django REST Framework (DRF). It focuses on setting up the environment, defining a custom user model, and implementing a robust token-based authentication system.

🚀 Key Features
Custom User Model: Extends Django's AbstractUser to include social media-specific fields like bio, profile_picture, and followers (a many-to-many relationship allowing users to follow each other).

Token Authentication: Utilizes Django REST Framework's TokenAuthentication for secure and stateless user authentication. Each authenticated user receives a unique token for accessing protected resources.

User Management Endpoints: Provides essential API endpoints for user registration, login, and personal profile management.

Media Handling: Configured to handle user-uploaded profile pictures, storing them securely within the project's media directory.

🛠️ Getting Started (Quick Setup)
To get this API up and running:

Install Dependencies:

pip install django djangorestframework Pillow

Project & App Creation:
Navigate to your desired project directory and run:

django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts

Configure settings.py:
Add 'rest_framework', 'rest_framework.authtoken', and 'accounts' to INSTALLED_APPS. Set AUTH_USER_MODEL = 'accounts.User' and configure MEDIA_URL/MEDIA_ROOT.

Run Migrations:

python manage.py makemigrations accounts
python manage.py makemigrations
python manage.manage.py migrate

Start Server:

python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/.

🔑 Authentication Endpoints
All authentication-related endpoints are under the /api/accounts/ prefix.

POST /api/accounts/register/:

Purpose: Create a new user account.

Input: username, email, password, password2, bio (optional), profile_picture (optional).

Output: 201 Created status with user details and an authentication token.

POST /api/accounts/login/:

Purpose: Authenticate an existing user.

Input: username, password.

Output: 200 OK status with user ID, email, username, and the authentication token.

GET, PUT, PATCH /api/accounts/profile/:

Purpose: Retrieve or update the authenticated user's profile.

Authentication: Requires an Authorization: Token <your_token> header.

Output (GET): 200 OK status with the user's profile details.

Input (PUT/PATCH): JSON body with fields to update (e.g., {"bio": "New bio"}).

This API provides a solid foundation for building social interactions and managing user identities within your application.