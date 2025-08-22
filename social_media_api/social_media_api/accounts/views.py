
    
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from .models import User # Import your custom User model

class RegisterAPIView(generics.CreateAPIView):
    """
    API view for user registration.
    Handles POST requests to create a new user and returns user data and a token.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny] # Anyone can register
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.get_or_create(user=user) # Create a token for the new user

class LoginAPIView(ObtainAuthToken):
    """
    API view for user login.
    Handles POST requests to authenticate a user and returns a token.
    Uses DRF's built-in ObtainAuthToken for token generation.
    """
    serializer_class = UserLoginSerializer # Use your custom login serializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating the authenticated user's profile.
    Requires authentication.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Returns the User instance for the currently authenticated user.
        """
        return self.request.user

