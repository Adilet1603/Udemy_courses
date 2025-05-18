from rest_framework import permissions



class CheckUserRole(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'student':
            return True
        return False


class CheckCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, **kwargs):
        if request.method in permissions.SAFE_METHODS:
            return True
        return object.author == request.user