from rest_framework import permissions
from .models import User


class IsPersonnel(permissions.BasePermission):
    """
    Allows access only to Provider
    """

    def has_permission(self, request, view):
        return request.user.profession == "BP"

class IsCustomer(permissions.BasePermission):
    """
    Allows access only to Provider
    """

    def has_permission(self, request, view):
        return request.user.profession == "CT"

class IsProvider(permissions.BasePermission):
    """
    Allows access only to Provider
    """

    def has_permission(self, request, view):
        return request.user.profession == "PR"
