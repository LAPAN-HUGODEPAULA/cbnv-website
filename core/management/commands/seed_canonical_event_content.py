from datetime import date

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from wagtail.models import Site

from core.models import CoreSettings
from sponsors.models import Sponsor, SponsorTier


VENUE_ADDRESS = (
    "Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.\n"
    "R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901"
)


CANONICAL_SETTINGS = {
    "event_name": "XII Congresso Brasileiro de Neurociências da Visão",
    "short_event_name": "CBNV 2026",
    "edition": "XII",
    "theme": "Neurovisão na Era da Inteligência Artificial",
    "dates": "11 a 13 de novembro de 2026",
    "start_date": date(2026, 11, 11),
    "end_date": date(2026, 11, 13),
    "format_label": "Presencial com transmissão híbrida",
    "location": VENUE_ADDRESS,
    "city": "Belo Horizonte",
    "state": "Minas Gerais",
    "country": "Brasil",
    "venue_name": "Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha",
    "venue_short_name": "CAD-1/UFMG",
    "google_maps_url": "https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6",
}


PROTECTED_DEFAULTS = {
    "fapemig_text": "Apoio institucional: FAPEMIG - Fundação de Amparo à Pesquisa do Estado de Minas Gerais.",
    "default_seo_title": "CBNV 2026 | XII Congresso Brasileiro de Neurociências da Visão",
    "default_seo_description": (
        "XII Congresso Brasileiro de Neurociências da Visão, de 11 a 13 de novembro "
        "de 2026, no CAD-1/UFMG, em Belo Horizonte."
    ),
}


SUPPORTING_TIER = {
    "name": "Apoio institucional e científico",
    "slug": "apoio-institucional-e-cientifico",
    "weight": 4,
    "sort_order": 10,
}


SUPPORTING_ENTITIES = [
    {
        "name": "UFMG",
        "category": Sponsor.Category.ORGANIZING_INSTITUTION,
        "sort_order": 10,
        "show_on_home": True,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "FUNDEP",
        "category": Sponsor.Category.INSTITUTIONAL_PARTNER,
        "sort_order": 20,
        "show_on_home": True,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "FAPEMIG",
        "category": Sponsor.Category.FUNDING_AGENCY,
        "sort_order": 30,
        "show_on_home": True,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "Sociedade Brasileira de Neurovisão",
        "category": Sponsor.Category.SCIENTIFIC_PARTNER,
        "sort_order": 40,
        "show_on_home": True,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "Hospital de Olhos de Minas Gerais / HOLHOS",
        "category": Sponsor.Category.INSTITUTIONAL_PARTNER,
        "sort_order": 50,
        "show_on_home": True,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "UFRJ",
        "category": Sponsor.Category.SCIENTIFIC_PARTNER,
        "sort_order": 60,
        "show_on_home": False,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "USP",
        "category": Sponsor.Category.SCIENTIFIC_PARTNER,
        "sort_order": 70,
        "show_on_home": False,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "UFRN",
        "category": Sponsor.Category.SCIENTIFIC_PARTNER,
        "sort_order": 80,
        "show_on_home": False,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
    {
        "name": "UEMG",
        "category": Sponsor.Category.SCIENTIFIC_PARTNER,
        "sort_order": 90,
        "show_on_home": False,
        "show_in_footer": True,
        "show_on_about": True,
        "show_on_sponsorship": False,
    },
]


class Command(BaseCommand):
    help = "Seed canonical CBNV 2026 event settings and supporting entities."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Report the changes that would be made without writing to the database.",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite protected manually editable fields such as SEO text and FAPEMIG text.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        force = options["force"]

        site = Site.objects.filter(is_default_site=True).first() or Site.objects.first()
        if not site:
            raise CommandError("No Wagtail Site exists. Run migrations and create a site before seeding content.")

        self.stdout.write("Seed canonical event content")

        settings_created, settings_updated = self.seed_settings(site, dry_run=dry_run, force=force)
        tier_created, entities_created, entities_updated, entities_skipped = self.seed_supporting_entities(
            dry_run=dry_run
        )

        if dry_run:
            transaction.set_rollback(True)

        settings_status = "created" if settings_created else "updated" if settings_updated else "skipped"
        tier_status = "created" if tier_created else "available"
        self.stdout.write(f"Settings: {settings_status}")
        self.stdout.write(f"Supporting tier: {tier_status}")
        self.stdout.write(
            "Supporting entities: "
            f"{entities_created} created, {entities_updated} updated, {entities_skipped} skipped"
        )
        self.stdout.write("Announcements: skipped")
        self.stdout.write("Done")

    def seed_settings(self, site, *, dry_run, force):
        settings_qs = CoreSettings.objects.filter(site=site)
        settings = settings_qs.first()
        created = settings is None
        if created:
            settings = CoreSettings(site=site)

        changed = False
        for field, value in CANONICAL_SETTINGS.items():
            if getattr(settings, field) != value:
                setattr(settings, field, value)
                changed = True

        for field, value in PROTECTED_DEFAULTS.items():
            if force or not getattr(settings, field):
                if getattr(settings, field) != value:
                    setattr(settings, field, value)
                    changed = True

        changed |= self.set_pending_link_state(settings, "registration")
        changed |= self.set_pending_link_state(settings, "livestream")

        if created or changed:
            if not dry_run:
                settings.save()
            return created, changed
        return False, False

    def set_pending_link_state(self, settings, prefix):
        link_field = f"{prefix}_link"
        status_field = f"{prefix}_status"

        if getattr(settings, link_field):
            return False
        if getattr(settings, status_field) == CoreSettings.LinkStatus.COMING_SOON:
            return False

        setattr(settings, status_field, CoreSettings.LinkStatus.COMING_SOON)
        return True

    def seed_supporting_entities(self, *, dry_run):
        tier, tier_created = SponsorTier.objects.get_or_create(
            slug=SUPPORTING_TIER["slug"],
            defaults={
                "name": SUPPORTING_TIER["name"],
                "weight": SUPPORTING_TIER["weight"],
                "sort_order": SUPPORTING_TIER["sort_order"],
            },
        )

        if not tier_created:
            tier_changed = False
            for field in ("name", "weight", "sort_order"):
                if getattr(tier, field) != SUPPORTING_TIER[field]:
                    setattr(tier, field, SUPPORTING_TIER[field])
                    tier_changed = True
            if tier_changed and not dry_run:
                tier.save(update_fields=["name", "weight", "sort_order"])

        created = 0
        updated = 0
        skipped = 0

        for entity in SUPPORTING_ENTITIES:
            sponsor, sponsor_created = Sponsor.objects.get_or_create(
                name=entity["name"],
                defaults={**entity, "tier": tier, "status": Sponsor.Status.ACTIVE},
            )
            if sponsor_created:
                created += 1
                continue

            changed_fields = []
            expected = {**entity, "tier": tier, "status": Sponsor.Status.ACTIVE}
            for field, value in expected.items():
                if getattr(sponsor, field) != value:
                    setattr(sponsor, field, value)
                    changed_fields.append(field)

            if changed_fields:
                updated += 1
                if not dry_run:
                    sponsor.save(update_fields=changed_fields)
            else:
                skipped += 1

        return tier_created, created, updated, skipped
