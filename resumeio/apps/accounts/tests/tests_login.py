from django.test import TestCase
from django.urls import reverse, resolve
from ..views import SignUpView
from django.contrib.auth import forms
from ..models import User


class LoginTests(TestCase):
    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, forms.AuthenticationForm)

    def test_contains_signup_url(self):
        signup_url= reverse('signup')
        self.assertContains(self.response, 'href="{0}"'.format(
            signup_url
        ))


class SuccessfulLoginTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'test@gmail.com',
            'email': 'test@gmail.com',
            'password1': 'xasr@1234',
            'password2': 'xasr@1234'
        }
        self.client.post(url, data)
        login_url = reverse('login')
        login_data = {
            'email': 'test@gmail.com',
            'password1': 'xasr@1234',
        }
        self.response = self.client.post(login_url, data)

    def test_user_login_successful(self):
        print(self.response.status_code)

        self.assertTrue(User.objects.exists())