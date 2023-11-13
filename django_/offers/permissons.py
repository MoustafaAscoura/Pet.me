from rest_framework import permissions

class OfferPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action in ['list','retrieve'] or (view.action == 'destroy' and request.user.is_authenticated)
            
    def has_object_permission(self, request, view, obj):
        return view.action == 'retrieve' or (view.action == 'destroy' and obj.user == request.user)


class RequestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'destroy']:
            if request.parser_context['kwargs'].get('offer_id'):
                return request.user.is_authenticated and request.user.offers.filter(id=request.parser_context['kwargs'].get('offer_id')).exists()
            else:
                return request.user.is_authenticated
            
        elif view.action == 'requestAdopt':
            return request.user.is_authenticated and not request.user.offers.filter(id=request.parser_context['kwargs'].get('offer_id')).exists()

        else:
            return True

    def has_object_permission(self, request, view, obj):
        return request.user in [obj.user, obj.offer.user] 

