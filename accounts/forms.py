from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    def __init__(self, request, *args, **kwargs):
        super(AccountLoginForm, self).__init__(
            request=request, *args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'
