from Django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTests(TestCase):
    """To  test the user created for the new emial """

    def test_create_user_with_emial_successful(self):
        """Test a creating a new user with email address """
        email = "test@londonappdev.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )
        self.assertEqual(user.email,email)
        self.assertEqual(user.check_password(password))
