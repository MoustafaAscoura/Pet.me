from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.sender, request.user)
        return view.action in ['destroy'] and obj.sender == request.user
    