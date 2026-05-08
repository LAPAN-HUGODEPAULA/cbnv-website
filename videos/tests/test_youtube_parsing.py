import pytest
from django.core.exceptions import ValidationError

from videos.models import VideoResource, parse_youtube_url


class TestParseYouTubeURL:
    def test_standard_watch_url(self):
        result = parse_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        assert result["type"] == "video"
        assert result["video_id"] == "dQw4w9WgXcQ"

    def test_youtu_be_short_url(self):
        result = parse_youtube_url("https://youtu.be/dQw4w9WgXcQ")
        assert result["type"] == "video"
        assert result["video_id"] == "dQw4w9WgXcQ"

    def test_playlist_url(self):
        result = parse_youtube_url("https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf")
        assert result["type"] == "playlist"
        assert result["playlist_id"] == "PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"

    def test_channel_handle_url(self):
        result = parse_youtube_url("https://www.youtube.com/@congressoneurovis%C3%A3o")
        assert result["type"] == "channel"
        assert "congressoneurovis" in result["channel_handle"]

    def test_channel_handle_simple(self):
        result = parse_youtube_url("https://www.youtube.com/@testchannel")
        assert result["type"] == "channel"
        assert result["channel_handle"] == "testchannel"

    def test_invalid_url(self):
        result = parse_youtube_url("https://example.com/not-youtube")
        assert result["type"] is None

    def test_empty_string(self):
        result = parse_youtube_url("")
        assert result["type"] is None

    def test_no_www_prefix(self):
        result = parse_youtube_url("https://youtube.com/watch?v=abc123XYZ01")
        assert result["type"] == "video"
        assert result["video_id"] == "abc123XYZ01"


@pytest.mark.django_db
class TestVideoResourceValidation:
    def test_create_valid_video(self):
        vr = VideoResource(
            title="Test Video",
            youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
        vr.full_clean()
        assert vr.video_type == "video"
        assert vr.youtube_video_id == "dQw4w9WgXcQ"

    def test_create_valid_playlist(self):
        vr = VideoResource(
            title="Test Playlist",
            youtube_url="https://www.youtube.com/playlist?list=PLabc123",
        )
        vr.full_clean()
        assert vr.video_type == "playlist"
        assert vr.youtube_playlist_id == "PLabc123"

    def test_create_valid_channel(self):
        vr = VideoResource(
            title="CBNV Channel",
            youtube_url="https://www.youtube.com/@congressoneurovis%C3%A3o",
        )
        vr.full_clean()
        assert vr.video_type == "channel"
        assert vr.channel_handle != ""

    def test_reject_invalid_url(self):
        vr = VideoResource(
            title="Bad URL",
            youtube_url="https://vimeo.com/12345",
        )
        with pytest.raises(ValidationError) as exc_info:
            vr.full_clean()
        assert "youtube_url" in exc_info.value.message_dict
