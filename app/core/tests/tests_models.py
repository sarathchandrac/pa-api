from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = "test@email.com"
        password = "pass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the new user email is normalized """
        email = 'test@Mail.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test new user without email raises an error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='tet123'
            )

    def test_create_new_user(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_super_user(
            email='email@mail.com',
            password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
