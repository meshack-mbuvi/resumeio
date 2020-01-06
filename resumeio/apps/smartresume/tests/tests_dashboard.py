from django.test import TestCase
from django.urls import reverse, resolve

class DashboardTests(TestCase):
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
        self.client.post(login_url, login_data)

        dashboard_url = reverse('smart_resume:dashboard')
        self.response = self.client.get(dashboard_url)

    def test_can_get_home(self):
        home_url = reverse('smart_resume:home')
        response = self.client.get(home_url)
        self.assertEqual(self.response.status_code, 200)

    def test_can_get_dashboard(self):
        self.assertEqual(self.response.status_code, 200)

    def test_can_see_home_title_text(self):
        self.assertContains(self.response, '<div class="home-title">')

    def test_can_see_sub_title_text(self):
        self.assertContains(self.response, '<div class="sub-title">')

    def test_can_see_link_to_create_resume(self):
        create_resume_link = reverse('smart_resume:create-resume')
        self.assertContains(
            self.response, 'href="{0}"'
            .format(create_resume_link))
