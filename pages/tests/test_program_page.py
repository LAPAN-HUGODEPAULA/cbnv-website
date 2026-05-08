import pytest
from datetime import date, time
from pages.models import ProgramPage
from program.models import (
    ProgramDay, ProgramSession, ProgramTalk,
    CONFIRMED, PENDING, HIDDEN, PUBLISHED, DRAFT,
    TALK, BREAK, IN_PERSON
)
from wagtail.models import Page

@pytest.mark.django_db
class TestProgramPage:
    def setup_method(self):
        self.root = Page.objects.get(id=1)
        self.home = self.root.get_children().first()
        self.program_page = ProgramPage(title="Programação")
        self.home.add_child(instance=self.program_page)
        
        self.day = ProgramDay.objects.create(
            date=date(2026, 11, 11),
            title="Dia 1",
            sort_order=1
        )

    def test_get_context_filters_published_sessions(self):
        # Published session
        s1 = ProgramSession.objects.create(
            day=self.day, start_time=time(9, 0), end_time=time(10, 0),
            title="Session 1", activity_type=TALK, status=PUBLISHED
        )
        # Draft session (should be filtered out)
        s2 = ProgramSession.objects.create(
            day=self.day, start_time=time(10, 0), end_time=time(11, 0),
            title="Session 2", activity_type=TALK, status=DRAFT
        )
        
        # Add a confirmed talk to both
        ProgramTalk.objects.create(session=s1, title="Talk 1", status=CONFIRMED)
        ProgramTalk.objects.create(session=s2, title="Talk 2", status=CONFIRMED)
        
        context = self.program_page.get_context(None)
        program_data = context["program_data"]
        
        assert len(program_data) == 1
        assert len(program_data[0]["sessions"]) == 1
        assert program_data[0]["sessions"][0]["session"].title == "Session 1"

    def test_get_context_filters_confirmed_talks(self):
        s1 = ProgramSession.objects.create(
            day=self.day, start_time=time(9, 0), end_time=time(10, 0),
            title="Session 1", activity_type=TALK, status=PUBLISHED
        )
        
        ProgramTalk.objects.create(session=s1, title="Confirmed Talk", status=CONFIRMED)
        ProgramTalk.objects.create(session=s1, title="Pending Talk", status=PENDING)
        ProgramTalk.objects.create(session=s1, title="Hidden Talk", status=HIDDEN)
        
        context = self.program_page.get_context(None)
        program_data = context["program_data"]
        
        assert len(program_data[0]["sessions"][0]["talks"]) == 1
        assert program_data[0]["sessions"][0]["talks"][0].title == "Confirmed Talk"

    def test_get_context_includes_sessions_without_talks_if_special_type(self):
        # Break session (no talks needed)
        ProgramSession.objects.create(
            day=self.day, start_time=time(10, 0), end_time=time(11, 0),
            title="Coffee Break", activity_type=BREAK, status=PUBLISHED
        )
        
        context = self.program_page.get_context(None)
        program_data = context["program_data"]
        
        assert len(program_data[0]["sessions"]) == 1
        assert program_data[0]["sessions"][0]["session"].title == "Coffee Break"

    def test_get_context_excludes_empty_days(self):
        # Day with only draft sessions or no sessions
        day2 = ProgramDay.objects.create(
            date=date(2026, 11, 12),
            title="Dia 2",
            sort_order=2
        )
        ProgramSession.objects.create(
            day=day2, start_time=time(9, 0), end_time=time(10, 0),
            title="Draft Session", activity_type=TALK, status=DRAFT
        )
        
        context = self.program_page.get_context(None)
        program_data = context["program_data"]
        
        # Only Dia 1 (from setup) should be here if we add something to it
        s1 = ProgramSession.objects.create(
            day=self.day, start_time=time(9, 0), end_time=time(10, 0),
            title="Session 1", activity_type=BREAK, status=PUBLISHED
        )
        
        context = self.program_page.get_context(None)
        program_data = context["program_data"]
        
        assert len(program_data) == 1
        assert program_data[0]["day"].title == "Dia 1"

    def test_program_page_renders_empty_state(self, client):
        response = client.get(self.program_page.url)
        html = response.content.decode()

        assert "A programação será disponibilizada em breve." in html
