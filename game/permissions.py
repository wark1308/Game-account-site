from rest_framework.permissions import BasePermission



class IsCompanyOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.company.owner