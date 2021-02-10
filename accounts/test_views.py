from django.test import TestCase
from django.contrib.auth.models import User
from .forms import AccountSignUpForm

# Create your tests here.


class TestViews(TestCase):

    def test_get_signup_page(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_get_signup_complete_page(self):
        session = self.client.session
        session['email'] = 'test@test.com'
        session['username'] = 'Test User'
        session.save()
        response = self.client.get(
            '/signup/complete/', {'user_email': self.client.session.get('email')})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup_complete.html')

    def test_can_create_user(self):
        response = self.client.post(
            '/signup/payment/', {'username': 'Test User', 'email': 'test@test.com', 'password1': 'Testing@1234', 'password2': 'Testing@1234'})
        self.assertRedirects(response, '/signup/')
