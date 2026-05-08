from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import User


class UserModelTest(TestCase):
    def test_create_user_with_profile_fields(self):
        user = User.objects.create_user(
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
        user = User.objects.create_user(
            username="reviewer",
            email="reviewer@example.com",
            password="testpass123",
            is_reviewer=True,
        )
        self.assertFalse(user.is_author)
        self.assertTrue(user.is_reviewer)
        self.assertFalse(user.is_chair)

    def test_user_can_have_multiple_roles(self):
        user = User.objects.create_user(
            username="author_reviewer",
            email="ar@example.com",
            password="testpass123",
            is_author=True,
            is_reviewer=True,
        )
        self.assertTrue(user.is_author)
        self.assertTrue(user.is_reviewer)
        self.assertFalse(user.is_chair)

    def test_str_returns_full_name(self):
        user = User(
            username="jdoe",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(str(user), "John Doe")

    def test_str_falls_back_to_username(self):
        user = User(username="jdoe")
        self.assertEqual(str(user), "jdoe")

    def test_filter_by_role(self):
        User.objects.create_user(username="a1", is_author=True, password="p")
        User.objects.create_user(username="r1", is_reviewer=True, password="p")
        User.objects.create_user(username="c1", is_chair=True, password="p")
        self.assertEqual(User.objects.filter(is_reviewer=True).count(), 1)
        self.assertEqual(User.objects.filter(is_author=True).count(), 1)
        self.assertEqual(User.objects.filter(is_chair=True).count(), 1)


class UserRoleEnforcementTest(TestCase):
    def test_user_with_no_role_fails_validation(self):
        user = User(
            username="norole",
            email="norole@example.com",
            first_name="No",
            last_name="Role",
        )
        with self.assertRaises(ValidationError):
            user.clean()

    def test_author_role_passes_validation(self):
        user = User(username="author1", is_author=True)
        user.clean()

    def test_reviewer_role_passes_validation(self):
        user = User(username="reviewer1", is_reviewer=True)
        user.clean()

    def test_chair_role_passes_validation(self):
        user = User(username="chair1", is_chair=True)
        user.clean()

    def test_staff_user_passes_validation(self):
        user = User(username="staff1", is_staff=True)
        user.clean()

    def test_superuser_passes_validation(self):
        user = User(username="super1", is_superuser=True)
        user.clean()

    def test_multiple_roles_pass_validation(self):
        user = User(
            username="multi",
            is_author=True,
            is_reviewer=True,
            is_chair=True,
        )
        user.clean()
