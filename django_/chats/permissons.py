from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'destroy' and request.method == 'DELETE':
            # Only allow authenticated users to delete specific messages using DELETE method
            return request.user.is_authenticated
        elif view.action == 'list' and request.method == 'GET':
            # Only allow authenticated users to get all messages associated with the current user using GET method
            return request.user.is_authenticated
        elif view.action == 'create' and request.method == 'POST':
            # Only allow authenticated users to create a new message to another user using POST method
            return request.user.is_authenticated
        return False
