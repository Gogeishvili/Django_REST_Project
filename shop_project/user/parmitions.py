from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True 
        return request.user.is_authenticated  