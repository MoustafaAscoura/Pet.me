from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user.is_superuser  # Only allow the owner of the pet to update or delete it
        return True
