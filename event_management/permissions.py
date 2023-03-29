from django.contrib import admin
from rest_framework.permissions import SAFE_METHODS, \
    IsAuthenticated, BasePermission

CODENAME_METHOD = dict(
    GET="view",
    HEAD="view",
    OPTIONS="view",
    POST="add",
    PUT="change",
    PATCH="change",
    DELETE="delete",
)


def get_codename(request, view):
    method_name = CODENAME_METHOD.get(request.method.upper()) or ''
    basename = view.basename or ''
    return "_".join((method_name, basename))


class DjangoAdminPermission(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        has_perm = super().has_change_permission(request, obj)
        if request.user.is_superuser:
            return True
        if employee := obj:
            employee = obj.support_employee if hasattr(obj, 'support_employee') else \
                obj.sale_employee
        return obj is None or employee == request.user if has_perm else False

    def has_delete_permission(self, request, obj=None):
        has_perm = super().has_delete_permission(request, obj)
        if request.user.is_superuser:
            return True
        if employee := obj:
            employee = obj.support_employee if hasattr(obj, 'support_employee') else \
                obj.sale_employee
        return obj is None or employee == request.user if has_perm else False


class HasGroupPermission(BasePermission):

    def has_permission(self, request, view):
        codename = get_codename(request, view)

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(permissions__codename=codename).exists():
            return True
        return bool(request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(obj, 'support_employee') and obj.support_employee == \
                request.user:
            return True
        if hasattr(obj, 'sale_employee') and obj.sale_employee == \
                request.user:
            return True
        return bool(request.user.is_superuser)
