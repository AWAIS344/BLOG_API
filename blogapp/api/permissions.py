from rest_framework import permissions

class IsAuth(permissions.BasePermission):
    """
    Custom permission to allow only the post author or an admin to create posts.
    """

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
        
class IsAuthorOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated first
        if not request.user.is_authenticated:
            return False  # Unauthenticated users cannot edit/delete
        
        return request.user == obj.author or request.user.is_staff
                
