from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token # Import Token
from .models import post, Comment

User = get_user_model() # Get the active user model

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the custom User model.
    Used for retrieving user details.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following')
        read_only_fields = ('followers', 'following',)

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles creating a new user and returns user data along with a token.
    """
    # serializers.CharField() is used here for password
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    # serializers.CharField() is used here for password2
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField(read_only=True)

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
        and explicitly creates an authentication token for the user.
        """
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        token = Token.objects.create(user=user)
        user.auth_token_key = token.key
        return user

    def get_token(self, obj):
        """
        Returns the authentication token for the user object.
        """
        return getattr(obj, 'auth_token_key', None)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Takes username and password, authenticates, and returns user and token.
    """
    # serializers.CharField() is used here for username
    username = serializers.CharField(required=True)
    # serializers.CharField() is used here for password
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField(read_only=True)

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
        token, created = Token.objects.get_or_create(user=user)
        data['token_key'] = token.key
        return data

    def get_token(self, obj):
        """
        Returns the authentication token from the validated data.
        """
        return self.validated_data.get('token_key')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
        # Similar to CommentSerializer, timestamps are read-only.
        read_only_fields = ['created_at', 'updated_at']

