from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Пользователи могут выполнять любые действия, если они администраторы.
    Для всех остальных пользователей разрешены только GET запросы.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS
