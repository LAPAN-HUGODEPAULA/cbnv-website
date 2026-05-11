import pytest

from sponsors.models import Sponsor, SponsorTier


@pytest.mark.django_db
def test_supporting_entity_public_queries_respect_status_and_flags():
    tier = SponsorTier.objects.create(name="Apoio", slug="apoio", sort_order=1)
    footer_entity = Sponsor.objects.create(
        name="FAPEMIG",
        category=Sponsor.Category.FUNDING_AGENCY,
        tier=tier,
        status=Sponsor.Status.ACTIVE,
        show_in_footer=True,
        show_on_home=True,
        sort_order=2,
    )
    Sponsor.objects.create(
        name="Oculto",
        category=Sponsor.Category.SUPPORT,
        tier=tier,
        status=Sponsor.Status.HIDDEN,
        show_in_footer=True,
        show_on_home=True,
        sort_order=1,
    )
    Sponsor.objects.create(
        name="Somente patrocínio",
        category=Sponsor.Category.SPONSOR,
        tier=tier,
        status=Sponsor.Status.ACTIVE,
        show_in_footer=False,
        show_on_home=False,
        sort_order=3,
    )

    assert list(Sponsor.objects.for_footer()) == [footer_entity]
    assert list(Sponsor.objects.for_home()) == [footer_entity]


@pytest.mark.django_db
def test_supporting_entities_have_deterministic_ordering():
    tier = SponsorTier.objects.create(name="Parceiros", slug="parceiros", sort_order=1)
    second = Sponsor.objects.create(name="B", tier=tier, show_in_footer=True, sort_order=2)
    first = Sponsor.objects.create(name="A", tier=tier, show_in_footer=True, sort_order=1)

    assert list(Sponsor.objects.for_footer()) == [first, second]
