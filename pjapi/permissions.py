from rest_framework import permissions


class AdmFullIsAuthOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
