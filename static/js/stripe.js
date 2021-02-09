$(document).ready(function () {
    var buy_now_button = document.querySelector('#buy_now_btn');

    var stripe = Stripe('{{ stripe_public_key }}');

    buy_now_button.addEventListener('click', function (event) {
        stripe.redirectToCheckout({
            sessionId: '{{ session_id }}',
        }).then(function (result) {

        });
    });
});