from rest_framework import permissions

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_instructor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class CanAccessLesson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        course = obj.course

        if not user.is_authenticated:
            return False

        if course.instructor == user:
            return True

        if course in user.enrolled_courses.all():
            return True

        return False