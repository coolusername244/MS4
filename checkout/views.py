from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing to see here!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IUbcLFctfkBQlvnBFXGupaHPdNtCfrNBMIB8lMmg6xxs303LxVLKcPK2T7xJkDMfMxy1xa9ZFHMxG8iBWVi6Qzp00FJWoThu7',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
