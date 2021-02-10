from django.test import TestCase
from .forms import AccountSignUpForm

# Create your tests here.


class TestAccountSignUpForm(TestCase):
    def test_username_is_required(self):
        form = AccountSignUpForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_email_is_required(self):
        form = AccountSignUpForm({'username': 'Test User', 'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        
    def test_fields_are_explicit_in_form_meta_class(self):
        form = AccountSignUpForm()
        self.assertEqual(form.Meta.fields, ['username', 'email', 'password1', 'password2'])
