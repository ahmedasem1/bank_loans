from rest_framework import permissions
from .models import User


class IsPersonnel(permissions.BasePermission):
    """
    Allows access only to Provider
    """

    def has_permission(self, request, view):
        return request.user.type == "BP"


class IsCustomer(permissions.BasePermission):
    """
    Allows access only to Provider
    """

    def has_permission(self, request, view):
        return request.user.type == "CT"


class IsProvider(permissions.BasePermission):
    """
    Allows access only to Provider
    """

    def has_permission(self, request, view):
        return request.user.type == "PR"
