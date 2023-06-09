from rest_framework import permissions


class IsOrganizationOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.organization.owner == request.user or obj.user == request.user
