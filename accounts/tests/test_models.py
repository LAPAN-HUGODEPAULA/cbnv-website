from django.conf import settings
from django.test import TestCase

from accounts.models import User, UserProfile
from accounts.tests.factories import create_user_with_profile


class UserModelTest(TestCase):
    def test_project_uses_default_django_user(self):
        self.assertEqual(settings.AUTH_USER_MODEL, "auth.User")
        self.assertEqual(User._meta.label, "auth.User")

    def test_create_user_with_profile_fields(self):
        user = create_user_with_profile(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            first_name="Test",
            last_name="User",
            institution="UFMG",
            country="BR",
            position="Professor",
            is_author=True,
        )
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.get_full_name(), "Test User")
        self.assertEqual(user.institution, "UFMG")
        self.assertEqual(user.country, "BR")
        self.assertEqual(user.position, "Professor")

    def test_user_has_scientific_role_flags(self):
        user = create_user_with_profile(
            username="reviewer",
            email="reviewer@example.com",
            password="testpass123",
            is_reviewer=True,
        )
        self.assertFalse(user.is_author)
        self.assertTrue(user.is_reviewer)
        self.assertFalse(user.is_chair)

    def test_user_can_have_multiple_roles(self):
        user = create_user_with_profile(
            username="author_reviewer",
            email="ar@example.com",
            password="testpass123",
            is_author=True,
            is_reviewer=True,
        )
        self.assertTrue(user.is_author)
        self.assertTrue(user.is_reviewer)
        self.assertFalse(user.is_chair)

    def test_default_user_get_full_name(self):
        user = User(
            username="jdoe",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.get_full_name(), "John Doe")

    def test_str_falls_back_to_username(self):
        user = User(username="jdoe")
        self.assertEqual(str(user), "jdoe")

    def test_filter_by_role(self):
        create_user_with_profile(username="a1", is_author=True, password="p")
        create_user_with_profile(username="r1", is_reviewer=True, password="p")
        create_user_with_profile(username="c1", is_chair=True, password="p")
        self.assertEqual(User.objects.filter(profile__is_reviewer=True).count(), 1)
        self.assertEqual(User.objects.filter(profile__is_author=True).count(), 1)
        self.assertEqual(User.objects.filter(profile__is_chair=True).count(), 1)


class UserRoleEnforcementTest(TestCase):
    def test_user_with_no_role_is_allowed_for_pending_dashboard_state(self):
        user = User.objects.create_user(
            username="norole",
            email="norole@example.com",
            first_name="No",
            last_name="Role",
        )
        profile = user.profile
        profile.clean()
        self.assertFalse(profile.is_author)
        self.assertFalse(profile.is_reviewer)
        self.assertFalse(profile.is_chair)

    def test_author_role_passes_validation(self):
        user = User.objects.create_user(username="author1")
        profile = user.profile
        profile.is_author = True
        profile.clean()

    def test_reviewer_role_passes_validation(self):
        user = User.objects.create_user(username="reviewer1")
        profile = user.profile
        profile.is_reviewer = True
        profile.clean()

    def test_chair_role_passes_validation(self):
        user = User.objects.create_user(username="chair1")
        profile = user.profile
        profile.is_chair = True
        profile.clean()

    def test_staff_user_passes_validation(self):
        user = User.objects.create_user(username="staff1", is_staff=True)
        user.profile.clean()

    def test_superuser_passes_validation(self):
        user = User.objects.create_user(username="super1", is_superuser=True)
        user.profile.clean()

    def test_multiple_roles_pass_validation(self):
        user = User.objects.create_user(
            username="multi",
        )
        profile = user.profile
        profile.is_author = True
        profile.is_reviewer = True
        profile.is_chair = True
        profile.clean()
