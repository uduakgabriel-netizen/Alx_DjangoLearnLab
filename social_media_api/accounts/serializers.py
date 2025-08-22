# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model # NEW: Import get_user_model
from rest_framework.authtoken.models import Token # NEW: Import Token
# from .models import User # Removed direct import, using get_user_model() instead for clarity with checks

User = get_user_model() # NEW: Get the active user model

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the custom User model.
    Used for retrieving user details.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following')
        read_only_fields = ('followers', 'following',) # Followers/following handled separately

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles creating a new user and returns user data along with a token.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField(read_only=True) # Field to return the token

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture', 'token')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        """
        Validates that the two password fields match.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        """
        Creates and returns a new user instance, given the validated data,
        and generates an authentication token for the user.
        """
        # validated_data.pop('password2') 
        user = get_user_model().objects.create_user( # UPDATED: Explicit get_user_model() call
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        # NEW: Create a token for the user immediately after creation
        token, created = Token.objects.get_or_create(user=user) # Token.objects.get_or_create is here
        user.auth_token_key = token.key # Store the token key temporarily on the user object for get_token method
        return user

    def get_token(self, obj):
        """
        Returns the authentication token for the user object.
        This method is called because 'token' is a SerializerMethodField.
        """
        return getattr(obj, 'auth_token_key', None)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Takes username and password, authenticates, and returns user and token.
    """
    username = serializers.CharField(required=True) # serializers.CharField() is here
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}) # serializers.CharField() is here
    token = serializers.SerializerMethodField(read_only=True) # Field to return the token

    def validate(self, data):
        """
        Validates the username and password against the database.
        """
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        # NEW: Get or create the token for the authenticated user and attach it
        token, created = Token.objects.get_or_create(user=user) # Token.objects.get_or_create is here
        data['token_key'] = token.key # Store the token key in validated data for get_token method
        return data

    def get_token(self, obj):
        """
        Returns the authentication token from the validated data.
        """
        return self.validated_data.get('token_key')