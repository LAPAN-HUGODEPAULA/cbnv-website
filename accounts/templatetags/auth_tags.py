from django import template

register = template.Library()


@register.filter
def has_role(user, role):
    if not user or not user.is_authenticated:
        return False
    return getattr(user, f"is_{role}", False)
