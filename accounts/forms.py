from django.contrib.auth.forms import SetPasswordForm, UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField


class AccountSignUpForm(UserCreationForm):
    """
    Creates a user, with no privileges, from the given username, email and password.

    Args:
        UserCreationForm (class): Standard user creation form provided by Django. Can be found here: `django.contrib.auth.forms`
    """
    email = EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(AccountSignUpForm, self).__init__(*args, **kwargs)

        self.fields['password2'].label = 'Confirm Password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'


class AccountLoginForm(AuthenticationForm):
    """
    Custom Login Form which added some custom styling to the fields.

    Args:
        AuthenticationForm (class): Standard user login form provided by Django. Can be found here: `django.contrib.auth.forms`
    """

    def __init__(self, request, *args, **kwargs):
        super(AccountLoginForm, self).__init__(
            request=request, *args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'


class ResetPasswordForm(PasswordResetForm):
    """
    Custom Password reset Form which added some custom styling to the field.

    Args:
        PasswordResetForm (class): Standard password reset form provided by Django. Can be found here: `django.contrib.auth.forms`
    """

    def __init__(self):
        super(PasswordResetForm, self).__init__()

        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg border-0'


class AccountChangePasswordForm(SetPasswordForm):
    """
    Custom Password Change Form which added some custom styling to the fields.

    Args:
        PasswordChangeForm (class): Standard password set form provided by Django. Can be found here: `django.contrib.auth.forms`
    """

    def __init__(self, *args, **kwargs):
        super(AccountChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password2'].label = 'Confirm Password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'
