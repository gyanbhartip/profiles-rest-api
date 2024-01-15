from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    # this function is called every time a request is made to the API

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # safe methods are HTTP GET, HEAD, OPTIONS
        # if the request is a safe method, return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
