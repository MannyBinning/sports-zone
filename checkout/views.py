from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ItClxA4vjBOX4oj3IZiPTeY3V5qCAdGiGqYboyXPE3asWKkFfFhlvm7ZwJSxi6LYiORr6MHepqLDiY88TQLcBof00tJv7JE9A',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)