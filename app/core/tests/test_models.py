"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_succesfull(self):
        email = 'caio@mail.com'
        password = 'senha123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_whithout_email_raises_error(self):
        """Test that creating user without an email raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@mail.com',
            '132',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
