from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated  # Only allow authenticated users to create pets
        else:
            return True  # Deny all other actions

    def has_object_permission(self, request, view, obj):
        if view.action in ['destroy', 'partial_update', 'update']:
            return obj.owner == request.user  # Only allow the owner of the pet to update or delete it
        else:
            return True
