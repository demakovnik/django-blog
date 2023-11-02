import pytest

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from authentication.models import User


# Create your tests here.

class UserRegisterTest(TestCase):
    fixtures = ['authentication.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            'username': 'alex',
            'email': 'alex@mail.ru',
            'password1': 'MySuperStrongPassword123',
            'password2': 'MySuperStrongPassword123'
        }

        cls.user_broken_data = {
            'username': 'jake',
            'email': 'jake@mail.ru',
            'password1': 'MySuperStrongPassword123',
            'password2': 'MySuperStrongPassword1234'
        }

    def test_succ_register(self):
        response = self.client.get(
            #'/register/',
            reverse('authentication:register')
        )

        self.assertEqual(200, response.status_code)
        self.assertIn('Username:', response.content.decode())

        response = self.client.post(
            reverse('authentication:register'),
            data=self.user_data
        )

        self.assertEqual(302, response.status_code)

        new_user: User = get_user_model().objects.get(
            username=self.user_data['username']
        )

        self.assertEqual(self.user_data['email'],
                         new_user.email)

    def test_fail_register(self):
        response = self.client.post(
            reverse('authentication:register'),
            data=self.user_broken_data
        )

        self.assertEqual(200, response.status_code)
        self.assertFormError(
            response,
            'form',
            'password2',
            _('The two password fields didn’t match.')
        )

    def test_login(self):
        response = self.client.get(
            reverse('authentication:login')
        )
        self.assertEqual(200, response.status_code)
        self.client.login(username='nikita', password='HelloWorld123456')
        response = self.client.get('/')  # force login
        user_from_context: User = response.context['user']
        self.assertIsNotNone(user_from_context)
        self.assertTrue(user_from_context.is_authenticated)
        self.assertEqual(200, response.status_code)
