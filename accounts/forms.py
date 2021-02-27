from accounts.models import Account
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm, AuthenticationForm, PasswordResetForm
from django.forms.fields import EmailField, FileField
from django.forms import ModelForm


class AccountSignUpForm(UserCreationForm):
    """
    Creates a user, with no privileges, from the given username, email and password.

    Args:
        UserCreationForm (class): Standard user creation form provided by Django. Can be found here: `django.contrib.auth.forms`
    """
    email = EmailField(required=True, label='Email')

    class Meta:
        model = Account
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
    
    class Meta:
        model = Account
        fields = ['username', 'password']

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

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg border-0'


class AccountChangePasswordForm(SetPasswordForm):
    """
    Custom Password Change Form which added some custom styling to the fields.

    Args:
        PasswordChangeForm (class): Standard password set form provided by Django. Can be found here: `django.contrib.auth.forms`
    """
    
    class Meta:
        model = Account
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(AccountChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password2'].label = 'Confirm Password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'


class AccountUpdateForm(ModelForm):

    profile_picture = FileField(required=False, label='Profile Picture')

    class Meta:
        model = Account
        fields = ['profile_picture', 'first_name',
                  'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'

    def save(self):
        return super(AccountUpdateForm, self).save()
