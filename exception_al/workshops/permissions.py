from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
<<<<<<< HEAD
        return obj.owner == request.user
=======
        return request.user and request.user.is_authenticated
    
>>>>>>> 09fb8f9 ( resolving merge conflict for PR#6)
