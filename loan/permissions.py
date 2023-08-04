from rest_framework import permissions
from .models import User


# class IsPersonnelOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if User.type=="BP":
#             return super().has_permission(request, view)
#         else:

class IsPersonnelOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return User.type=="BP"        