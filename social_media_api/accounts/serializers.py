from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User # Import your custom User model

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
    Handles creating a new user.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')
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
        Creates and returns a new user instance, given the validated data.
        """
        validated_data.pop('password2') # Remove password2 as it's not a model field
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''), # Email can be optional
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Takes username and password, authenticates, and returns user and token.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

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
        return data

