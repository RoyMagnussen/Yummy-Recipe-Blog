from django.shortcuts import render
from .forms import AccountSignUpForm

# Create your views here.


def sign_up(request) -> render:
    """
    Renders the sign up view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse ojbect whose content is filled by the given template and context.
    """
    form = AccountSignUpForm()
    context = {
        'title': 'Sign Up',
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
