from django.test import TestCase
from django.urls import reverse, resolve
from ..views import SignUpView
from ..forms import SignUpForm
from django.contrib.auth.models import User


class SetUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_contains_login_url(self):
        login_url= reverse('login')
        self.assertContains(self.response, 'href="{0}"'.format(
            login_url
        ))


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'test@gmail.com',
            'email': 'test@gmail.com',
            'password1': 'xasr@1234',
            'password2': 'xasr@1234'
        }

        self.response = self.client.post(url, data)

    def test_user_creation_successful(self):
        self.assertTrue(User.objects.exists())


class UnsuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'email': 'test@gmail.com',
            'password1': 'xasr@1234',
            'password2': 'xasr@1234'
        }

        self.response = self.client.post(url, data)

    def test_user_creation_unsuccessful(self):
        self.assertFalse(User.objects.exists())