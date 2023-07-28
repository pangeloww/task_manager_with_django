from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from accounts.forms import CreateAccountForm
from accounts.models import User


class RegisterViewTest(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CreateAccountForm)

    def test_post_valid_data(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            # Include other required fields for your CreateAccountForm
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_post_invalid_data(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'mismatchedpassword',
            # Include other required fields for your CreateAccountForm
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())


class LoginUserViewTest(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
