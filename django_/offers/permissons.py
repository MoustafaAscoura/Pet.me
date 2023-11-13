from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        
        elif view.action == 'destroy':
            return request.user.is_authenticated
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        if view.action in ['destroy']:
            return obj.user == request.user  # Only allow the owner of the pet to update or delete it
        else:
            return True
