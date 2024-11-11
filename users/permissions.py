from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = 'Moder can only retrieve and update data.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """
    Only owners can manage their data.
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
