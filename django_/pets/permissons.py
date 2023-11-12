from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True  # Allow all users to list/view pets
        elif view.action == 'create':
            return request.user.is_authenticated  # Only allow authenticated users to create pets
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True  # Allow all users to retrieve, update, and delete pets
        else:
            return False  # Deny all other actions

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True  # Allow all users to retrieve (view) the pet
        elif view.action in ['update', 'partial_update', 'destroy']:
            return obj.owner == request.user  # Only allow the owner of the pet to update or delete it
        elif view.action == 'offerPet':
            return obj.owner == request.user  # Only allow the owner of the pet to make offers for adoption
        else:
            return False
