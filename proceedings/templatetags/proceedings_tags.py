from django import template

register = template.Library()


@register.filter
def youtube_embed_url(url):
    if not url:
        return ""
    from videos.models import parse_youtube_url

    parsed = parse_youtube_url(url)
    video_id = parsed.get("video_id", "")
    if video_id:
        return f"https://www.youtube.com/embed/{video_id}"
    return ""
