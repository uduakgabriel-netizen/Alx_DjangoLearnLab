from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken # Still needed for base class
from rest_framework.settings import api_settings
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from .models import User

class RegisterAPIView(generics.CreateAPIView):
    """
    API view for user registration.
    Handles POST requests to create a new user and returns user data and a token.
    The token is now returned by the serializer.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) # This calls serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class LoginAPIView(ObtainAuthToken): # Still inheriting from ObtainAuthToken for its base behavior
    """
    API view for user login.
    Handles POST requests to authenticate a user and returns a token.
    The token is now returned by the serializer.
    """
    serializer_class = UserLoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # The token is now part of serializer.data
        return Response(serializer.data)


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

