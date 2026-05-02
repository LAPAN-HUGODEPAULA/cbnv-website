from django.test import TestCase

from accounts.models import User


class UserModelTest(TestCase):
    def test_create_user_with_profile_fields(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            full_name="Test User",
            institution="UFMG",
            country="BR",
            position="Professor",
        )
        self.assertEqual(user.full_name, "Test User")
        self.assertEqual(user.institution, "UFMG")
        self.assertEqual(user.country, "BR")
        self.assertEqual(user.position, "Professor")

    def test_user_has_scientific_role_flags(self):
        user = User.objects.create_user(
            username="reviewer",
            email="reviewer@example.com",
            password="testpass123",
        )
        self.assertFalse(user.is_author)
        self.assertFalse(user.is_reviewer)
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
            full_name="John Doe",
        )
        self.assertEqual(str(user), "John Doe")

    def test_str_falls_back_to_username(self):
        user = User(username="jdoe", full_name="")
        self.assertEqual(str(user), "jdoe")

    def test_filter_by_role(self):
        User.objects.create_user(username="a1", is_author=True, password="p")
        User.objects.create_user(username="r1", is_reviewer=True, password="p")
        User.objects.create_user(username="u1", password="p")
        self.assertEqual(User.objects.filter(is_reviewer=True).count(), 1)
        self.assertEqual(User.objects.filter(is_author=True).count(), 1)
        self.assertEqual(User.objects.filter(is_chair=True).count(), 0)
