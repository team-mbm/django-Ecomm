"""
Only Customer who is owner of his account can manipulate attrs
"""
from rest_framework import permissions

class IsCustomerOwner(permissions.BasePermission):
    """
    check permission,if customer is owner of his account
    """
    def has_object_permission(self, request, view, customer):
        if request.user:
            return customer == request.user
        return False
