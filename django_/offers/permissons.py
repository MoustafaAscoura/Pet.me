from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'destroy' and request.user.is_authenticated:
            # Only allow authenticated users (offer owners) to delete offers using DELETE method
            return True
        elif view.action == 'list' and request.user.is_authenticated:
            # Only allow authenticated users (offer owners) to get all requests on their offers using GET method
            return True
        elif view.action == 'delete' and request.user.is_authenticated:
            # Only allow authenticated users (offer owners) to delete requests using DELETE method
            return True
        elif view.action == 'create' and request.method == 'POST':
            # Only allow authenticated users to send an adopt request using POST method
            return request.user.is_authenticated
        elif view.action == 'list' and request.user.is_authenticated:
            # Only allow authenticated users to get all requests on their offers using GET method
            return True
        elif view.action == 'accept' and request.user.is_authenticated:
            # Only allow authenticated users (offer owners) to accept requests
            return True
        return False
