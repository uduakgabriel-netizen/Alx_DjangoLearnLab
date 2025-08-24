from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    Read permissions are allowed to any authenticated user.
    Assumes the model instance has an 'author' attribute.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True # Allow read-only access for all requests
        return request.user and request.user.is_authenticated 
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

