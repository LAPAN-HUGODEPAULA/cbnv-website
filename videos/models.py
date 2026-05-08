import re

from django.core.exceptions import ValidationError
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import TranslatableMixin
from wagtail.snippets.models import register_snippet

VIDEO = "video"
PLAYLIST = "playlist"
CHANNEL = "channel"

VIDEO_TYPE_CHOICES = [
    (VIDEO, "Vídeo"),
    (PLAYLIST, "Playlist"),
    (CHANNEL, "Canal"),
]

DRAFT = "draft"
PUBLIC = "public"
HIDDEN = "hidden"

STATUS_CHOICES = [
    (DRAFT, "Rascunho"),
    (PUBLIC, "Público"),
    (HIDDEN, "Oculto"),
]

YOUTUBE_PATTERNS = [
    (re.compile(r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]{11})"), VIDEO, "video_id"),
    (re.compile(r"(?:https?://)?youtu\.be/([A-Za-z0-9_-]{11})"), VIDEO, "video_id"),
    (re.compile(r"(?:https?://)?(?:www\.)?youtube\.com/playlist\?list=([A-Za-z0-9_-]+)"), PLAYLIST, "playlist_id"),
    (re.compile(r"(?:https?://)?(?:www\.)?youtube\.com/@([A-Za-z0-9_.%-]+)"), CHANNEL, "channel_handle"),
]


def parse_youtube_url(url: str) -> dict:
    """Extract YouTube IDs and resource type from a URL.

    Returns dict with keys: type, video_id, playlist_id, channel_handle.
    """
    for pattern, res_type, key in YOUTUBE_PATTERNS:
        match = pattern.search(url)
        if match:
            return {"type": res_type, key: match.group(1)}
    return {"type": None}


@register_snippet
class VideoResource(TranslatableMixin, models.Model):
    title = models.CharField("Título", max_length=255)
    description = models.TextField("Descrição", blank=True)
    youtube_url = models.URLField("URL do YouTube")
    youtube_video_id = models.CharField("ID do Vídeo", max_length=20, blank=True, editable=False)
    youtube_playlist_id = models.CharField("ID da Playlist", max_length=50, blank=True, editable=False)
    channel_handle = models.CharField("Handle do Canal", max_length=100, blank=True, editable=False)
    video_type = models.CharField("Tipo", max_length=10, choices=VIDEO_TYPE_CHOICES, blank=True, editable=False)
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("youtube_url"),
        FieldPanel("status"),
    ]

    class Meta:
        ordering = ["-id"]
        verbose_name = "Vídeo / Recurso"
        verbose_name_plural = "Vídeos / Recursos"
        abstract = False
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_videos_videoresource",
            )
        ]

    def __str__(self):
        return self.title

    def clean(self):
        parsed = parse_youtube_url(self.youtube_url)
        if not parsed["type"]:
            raise ValidationError({"youtube_url": "URL do YouTube inválida. Use um link de vídeo, playlist ou canal."})
        self.video_type = parsed["type"]
        self.youtube_video_id = parsed.get("video_id", "")
        self.youtube_playlist_id = parsed.get("playlist_id", "")
        self.channel_handle = parsed.get("channel_handle", "")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
