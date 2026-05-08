from django import template
from wagtail.models import Site

from core.models import SiteMenu

register = template.Library()


FALLBACK_MENU = [
    ("Início", None, "/"),
    ("Sobre", "sobre", None),
    ("Programação", "programacao", None),
    ("Submissões", "submissoes", "/submissoes/"),
    ("Edições Anteriores", "edicoes-anteriores", None),
]


def _normalize_url(url):
    return url or "/"


def _streamfield_menu_items(site):
    menu = SiteMenu.for_site(site)
    items = []

    for item in menu.menu_items:
        link = item.value
        page = link.get("page")
        url = page.url if page else link.get("url")
        anchor = link.get("anchor") or ""

        if not url and not anchor:
            continue

        items.append(
            {
                "label": link.get("label"),
                "url": f"{_normalize_url(url)}{anchor}",
            }
        )

    return items


def _fallback_menu_items(site):
    root_page = site.root_page.specific
    children_by_slug = {
        page.slug: page.specific
        for page in root_page.get_children().live().public().specific()
    }

    items = []
    for label, slug, fallback_url in FALLBACK_MENU:
        if slug is None:
            url = root_page.url
        else:
            page = children_by_slug.get(slug)
            if page is None and fallback_url is None:
                continue
            url = page.url if page else fallback_url

        items.append({"label": label, "url": _normalize_url(url)})

    return items


@register.simple_tag(takes_context=True)
def public_menu_items(context):
    request = context.get("request")
    site = Site.find_for_request(request) if request else Site.objects.filter(is_default_site=True).first()

    if site is None:
        return [{"label": "Início", "url": "/"}]

    configured_items = _streamfield_menu_items(site)
    if configured_items:
        return configured_items

    return _fallback_menu_items(site)
