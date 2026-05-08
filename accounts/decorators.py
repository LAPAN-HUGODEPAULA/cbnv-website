from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def author_required(view_func=None):
    actual_decorator = user_passes_test(lambda u: u.is_authenticated and u.is_author)
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def reviewer_required(view_func=None):
    actual_decorator = user_passes_test(lambda u: u.is_authenticated and u.is_reviewer)
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def chair_required(view_func=None):
    actual_decorator = user_passes_test(lambda u: u.is_authenticated and u.is_chair)
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def complete_profile_required(view_func=None):
    def check(u):
        if not u.is_authenticated or not u.is_author:
            return False
        return u.has_complete_author_profile
    actual_decorator = user_passes_test(
        check,
        login_url="/conta/perfil/",
        redirect_field_name=None,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


class ReviewerMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_reviewer:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ChairMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_chair:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def admin_or_chair_required(view_func=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and (u.is_staff or u.is_superuser or u.is_chair)
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


class AdminOrChairMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not (
            request.user.is_staff or request.user.is_superuser or request.user.is_chair
        ):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
