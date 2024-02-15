from rest_framework import permissions

class PostsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['partial_update', 'update']:
            obj.user == request.user
        elif view.action == 'destroy':
            return (obj.user == request.user or request.user.is_superuser)
        elif view.action == 'hide':
            return request.user.is_superuser
        else:
            return True

class reportsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (view.action in ['create'] and request.user.is_authenticated) or request.user.is_superuser

class CommentsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (obj.user == request.user or request.user.is_superuser)
