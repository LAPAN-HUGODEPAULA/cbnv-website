import pytest

from submissions.models import ThematicAxis


@pytest.mark.django_db
class TestThematicAxis:
    def test_create_axis(self):
        axis = ThematicAxis.objects.create(name="Neurociência da Visão", order=1)
        assert str(axis) == "Neurociência da Visão"
        assert axis.name == "Neurociência da Visão"
        assert axis.order == 1

    def test_ordering(self):
        ThematicAxis.objects.create(name="Tecnologia Assistiva", order=4)
        ThematicAxis.objects.create(name="Oftalmologia Clínica", order=2)
        ThematicAxis.objects.create(name="Neurociência da Visão", order=1)
        axes = list(ThematicAxis.objects.all())
        assert axes[0].order == 1
        assert axes[1].order == 2
        assert axes[2].order == 4

    def test_unique_name(self):
        ThematicAxis.objects.create(name="Ergonomia Visual", order=1)
        from django.db import IntegrityError
        with pytest.raises(IntegrityError):
            ThematicAxis.objects.create(name="Ergonomia Visual", order=2)

    def test_fixture_data(self, db):
        from django.core.management import call_command
        call_command("loaddata", "thematic_axes", verbosity=0)
        assert ThematicAxis.objects.count() == 4
        names = list(ThematicAxis.objects.values_list("name", flat=True))
        assert "Neurociência da Visão" in names
        assert "Oftalmologia Clínica" in names
        assert "Ergonomia Visual" in names
        assert "Tecnologia Assistiva" in names

    def test_verbose_name(self):
        axis = ThematicAxis()
        assert axis._meta.verbose_name == "Eixo temático"
        assert axis._meta.verbose_name_plural == "Eixos temáticos"
