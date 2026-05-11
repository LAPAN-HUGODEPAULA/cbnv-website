from django import template

from sponsors.models import Sponsor

register = template.Library()


@register.simple_tag
def footer_supporting_entities(limit=6):
    return Sponsor.objects.for_footer()[:limit]
