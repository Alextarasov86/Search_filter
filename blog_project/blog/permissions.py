from rest_framework.permissions import BasePermission


class CanDeleteArticle(BasePermission):
    def has_permission(self, request, view):
        if request.method != 'DELETE':
            return True
        if request.user and request.user.has_perm('blog.delete_article'):
            return True
        return False

class CanAddArticle(BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            return True
        if request.user and request.user.has_perm('blog.add_article'):
            return True
        return False


class CanChangeArticle(BasePermission):
    def has_permission(self, request, view):
        if not request.method in ['PUT', 'PATCH']:
            return True
        if request.user and request.user.has_perm('blog.change_article'):
            return True
        return False


