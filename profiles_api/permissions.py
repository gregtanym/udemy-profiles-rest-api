# create custom permission class
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
        # how is user id going to be equal to obj id
        # how does returning true or false stop user from editing the profiles

# SAFE METHODS are methods that do not cause any destructive behaviour, such as GET, hence no permissions is required in our case