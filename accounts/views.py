from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from .forms import AccountChangePasswordForm, AccountSignUpForm, AccountLoginForm, ResetPasswordForm, AccountUpdateForm
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
import stripe
from django.contrib.auth.decorators import login_required
from .models import Account

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

    if request.user.is_authenticated:
        return redirect('home')
    else:
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
            form.is_active = True
            form.save(commit=True)
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


def reset_password(request) -> render:
    """
    Renders the reset password view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """

    form = ResetPasswordForm()
    context = {
        'title': 'Reset Password',
        'form': form,
    }

    if request.method == 'POST':
        user_email = request.POST['email']
        user = User.objects.get(email=user_email)
        token_generator = PasswordResetTokenGenerator()
        current_site = get_current_site(request)

        message_content = {
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user),
            'domain': current_site.domain,
        }

        link = reverse('reset_password_send', kwargs={
            'uidb64': message_content['uid'],
            'token': message_content['token'],
        })

        reset_url = 'http://'+current_site.domain+link

        email = EmailMessage(
            subject='Reset Your Password',
            body=f'Hi {user.username}!\n\nYou are seeing this email has you have requested to reset your password.\n\nPlease follow the link below to reset you password:\n{reset_url}',
            from_email=settings.EMAIL_HOST_USER,
            to=[user_email]
        )

        email.send(fail_silently=True)

        return redirect('reset_password_sent')

    return render(request, 'accounts/reset_password.html', context)


def reset_password_sent(request):
    """
    Renders the reset password sent view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """
    context = {
        'title': 'Email Sent',
    }

    return render(request, 'accounts/reset_password_sent.html', context)


def reset_password_change_password(request, uidb64, token):
    """
    Renders the reset password change password view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse object whose content is filled by the given template and context.
    """
    user_id = force_text(urlsafe_base64_decode(uidb64).decode())
    user = User.objects.get(pk=user_id)
    form = AccountChangePasswordForm(user)
    context = {
        'title': 'Change Password',
        'form': form,
    }

    if request.method == 'POST':

        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
        form = AccountChangePasswordForm(user, request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('new_password1')
            user.set_password(password)
            user.save()

        return redirect('reset_password_confirm')

    return render(request, 'accounts/reset_password_change_password.html', context)


def reset_password_confirm(request):
    context = {
        'title': 'Password Changed',
    }

    return render(request, 'accounts/reset_password_confirm.html', context)


def logout_user(request) -> redirect:
    """
    Logs out the current user and redirects to the log in page.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        redirect: Redirects the user to the provided url name.
    """
    logout(request)
    return redirect('login_page')


@login_required(login_url='/')
def update_user_page(request):
    user = Account.objects.get(username=request.user.username)
    form = AccountUpdateForm(instance=user)
    form.is_multipart()
    context = {
        'title': 'Update User',
        'user': user,
        'form': form,
    }
    
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, request.FILES, instance=user)
        form.is_multipart()
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    
    return render(request, 'accounts/update_user.html', context)