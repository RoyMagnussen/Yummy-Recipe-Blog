from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from .forms import AccountSignUpForm, AccountLoginForm, ResetPasswordForm
import stripe

# Create your views here.


def login_page(request) -> render:
    """
    Renders the login view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """
    form = AccountLoginForm(request)
    context = {
        'title': 'Log In',
        'form': form
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_page')

    return render(request, 'accounts/login.html', context)


def sign_up(request) -> render:
    """
    Renders the sign up view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """
    form = AccountSignUpForm()
    context = {
        'title': 'Sign Up',
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


def payment(request) -> render:
    """
    Renders the payment view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """
    if request.method == 'POST':
        form = AccountSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['email'] = form.cleaned_data.get('email')
            request.session['username'] = form.cleaned_data.get('username')

            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1IG9ejDG4AaONyVC9Xe2Trdy',
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('sign_up_complete')) + '?success_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('payment'))
            )

            context = {
                'title': 'Payment',
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
                'session_id': stripe_session.id,
            }

            return render(request, 'accounts/payment.html', context)

        else:
            return redirect('sign_up')

    elif request.method == 'GET':
        return redirect('sign_up')


def sign_up_complete(request) -> render:
    """
    Renders the signup complete view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """
    context = {
        'title': 'Sign Up Complete',
        'user_email': request.session['email']
    }

    username = request.session['username']
    subject = 'Yummy! Account Successfully Created!'
    email_body = f'Hi {username}!\n Welcome to the Yummy! family! We look forward to seeing you share some wonderful recipes with us.\n\n You are now able to log in.\n\nHappy cooking!\nThe Yummy! team.'

    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[request.session['email']],
    )
    email.send(fail_silently=True)

    return render(request, 'accounts/signup_complete.html', context)


def reset_password(request):
    form = ResetPasswordForm()
    context = {
        'title': 'Reset Password',
        'form': form,
    }
    return render(request, 'accounts/reset_password.html', context)
