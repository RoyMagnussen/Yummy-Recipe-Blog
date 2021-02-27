from django.test import TestCase
from .forms import AccountChangePasswordForm, AccountLoginForm, AccountSignUpForm, AccountUpdateForm, ResetPasswordForm

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
        self.assertEqual(form.Meta.fields, [
                         'username', 'email', 'password1', 'password2'])


class TestAccountLoginForm(TestCase):
    def test_username_is_required(self):
        form = AccountLoginForm({'username': ''})
        self.assertFalse(form.is_valid())

    def test_password_is_required(self):
        form = AccountLoginForm({'username': 'TestUser', 'passsword1': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        form = AccountLoginForm(self.client)
        self.assertEqual(form.Meta.fields, ['username', 'password'])


class TestResetPasswordForm(TestCase):
    def test_email_is_required(self):
        form = ResetPasswordForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')


class TestAccountChangePasswordForm(TestCase):
    def test_password1_is_required(self):
        form = AccountChangePasswordForm({'new_password': ''})
        self.assertFalse(form.is_valid())

    def test_password2_is_required(self):
        form = AccountChangePasswordForm(
            {'new_password': 'Testing@1234', 'new_password2': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        form = AccountChangePasswordForm(self)
        self.assertEqual(form.Meta.fields, ['new_password1', 'new_password2'])


class TestAccountUpdateForm(TestCase):
    def test_profile_picture_not_required(self):
        form = AccountUpdateForm({'profile_picture': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        form = AccountUpdateForm()
        self.assertEqual(form.Meta.fields, ['profile_picture', 'first_name',
                                            'last_name', 'username', 'email', 'password'])
