from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db.models import Max
from django.urls import reverse

# Create your tests here.

class UserLoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test4269')
        self.user2 = User.objects.create_user(username='testuser2', password='test42692')

    def test_login_status_code(self):
        """should be status code 200 if available"""

        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        """test whether login is successful, should redirect"""

        response = self.client.post(reverse('users:login'), {"username":'testuser', "password":'test4269'})

        self.assertEqual(response.status_code, 302)

    def test_login_fail(self):
        """test whether login is fail, no redirect"""

        response = self.client.post(reverse('users:login'), {"username":'testuser', "password":'sdasdasd'})

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """logout should redirect to login page, success should be code 200"""

        response = self.client.get(reverse('users:logout'))

        self.assertEqual(response.status_code, 200)

    def test_index_unavailable(self):
        """index can't be seen unless logged in, redirect to login page code 302"""
        response = self.client.get(reverse('users:index'))

        self.assertEqual(response.status_code, 302)

    def test_index_available(self):
        """index is available to be reached now"""

        self.client.force_login(self.user)
        response = self.client.get(reverse('users:index'))

        self.assertEqual(response.status_code, 200)