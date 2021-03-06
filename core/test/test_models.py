from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
		    email=email,
		    password=password
		)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
	    email = 'test@LONDONAPPDEV.com'
	    user = get_user_model().objects.create_user(email, 'test123')
	    self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)        



    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 302)