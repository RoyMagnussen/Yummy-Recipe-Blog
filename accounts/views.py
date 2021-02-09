from django.shortcuts import render
from django.shortcuts import redirect, render
from django.conf import settings
from django.urls import reverse
from .forms import AccountSignUpForm
import stripe

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


def payment(request) -> render:
    """
    Renders the payment view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse ojbect whose content is filled by the given template and context.
    """
    if request.method == 'POST':
        form = AccountSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['email'] = form.cleaned_data.get('email')

            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1IG9ejDG4AaONyVC9Xe2Trdy',
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('sign_up_complete')) + '?success_id={CHECKOUT_SESSION_ID}',
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
