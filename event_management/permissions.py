from rest_framework.permissions import SAFE_METHODS, \
    IsAuthenticated


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


class HasGroupPermission(IsAuthenticated):

    """
    Object-level permission to only allow contributors to access the projects.
    If the contributor permission is reader then he only can get the information.
    If the contributor permission is editor then he can modify the information.
    """

    def has_permission(self, request, view):
        codename = get_codename(request, view)

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(permissions__codename=codename).exists():
            return True
        return bool(request.user.is_superuser)
