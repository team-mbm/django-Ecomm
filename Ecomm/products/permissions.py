"""
Only Customer who is owner of his account can manipulate attrs
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    admin have all permissions(CRUD) whereas others(authenticated or annonyms)
    can only view i.e only GET permission
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.user.is_staff:
            return True
    def has_object_permission(self, request, view, obj):
        """
        admin can update,delete product but others can only view
        """
        if request.method == 'GET':
            return True
        elif request.user.is_staff:
            return True
        else:
            return False
