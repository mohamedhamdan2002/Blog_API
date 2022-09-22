from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        # authenticated user only can see list view
        if request.user.is_authenticated:
            return True
        return False
    
    
    def has_object_permission(self, request, view, obj):
        #read permissions are allowed to any request so we 'll always
        # allow Get, head, or options requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to the author of a post 
        return obj.author ==request.user