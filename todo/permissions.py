from rest_framework.permissions import BasePermission

class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request,view)

class ReadOnlyDetail(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and request.user
