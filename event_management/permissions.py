# from rest_framework.permissions import SAFE_METHODS, \
#     IsAdminUser
# from .models import Contributor
#
#
# class IsContributor(IsAdminUser):
#     """
#     Object-level permission to only allow contributors to access the projects.
#     If the contributor permission is reader then he only can get the information.
#     If the contributor permission is editor then he can modify the information.
#     """
#
#     def has_permission(self, request, view):
#
#         if not request.user.is_authenticated:
#             return False
#
#         project_id = view.kwargs.get('project_pk')
#         queryset = Contributor.objects.filter(project_id=project_id, user=request.user)
#         if queryset.filter(permission="editor").exists():
#             return True
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         elif queryset.filter(permission="reader").exists() \
#                 and request.method in SAFE_METHODS:
#             return True
#         return super(IsContributor, self).has_permission(request, view)
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         if hasattr(obj, 'author_user') and obj.author_user == request.user:
#             return True
#         if request.user.is_staff:
#             return True
#         return False
