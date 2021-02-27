from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .forms import AccountSignUpForm

# Create your tests here.


class TestViews(TestCase):
    
    def test_get_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

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
        
    def test_get_reset_password_page(self):
        response = self.client.get('/reset_password/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/reset_password.html')
        
    def test_get_reset_password_sent_page(self):
        response = self.client.get('/reset_password_sent/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/reset_password_sent.html')
        
    def test_get_reset_password_change_password_page(self):
        user = User.objects.create(username='Test User', email='test@test.com', password='Testing@1234')
        user.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        response = self.client.get(f'/reset_password/{uid}/{token}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/reset_password_change_password.html')
        
    def test_get_reset_password_confirm_page(self):
        response = self.client.get('/reset_password_confirm/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/reset_password_confirm.html')
        
    def test_get_update_user_page(self):
        response = self.client.get('/profile/edit/')
        self.assertEqual(response.status_code, 302)