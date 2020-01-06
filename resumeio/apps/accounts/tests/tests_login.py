from django.test import TestCase
from django.urls import reverse, resolve
from ..views import SignUpView
from django.contrib.auth import forms
from django.contrib.auth.models import User


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
            'username': 'test',
            'email': 'test@gmail.com',
            'password1': 'xasr@1234',
            'password2': 'xasr@1234'
        }
        self.client.post(url, data)
        login_url = reverse('login')
        login_data = {
            'username': 'test',
            'password': 'xasr@1234',
        }
        self.home_url = reverse('smart_resume:dashboard')
        self.response = self.client.post(login_url, login_data)

    def test_user_login_successful(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)