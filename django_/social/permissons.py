from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create' and request.method == 'POST':
            # Only allow authenticated users to create a post, report, comment, or reply using POST method
            return request.user.is_authenticated
        elif view.action in ['update', 'partial_update', 'destroy'] and request.user.is_authenticated:
            # Only allow authenticated users (post, comment, or reply owners) to update or delete a post, comment, or reply
            return True
        return False
