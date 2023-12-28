from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
import stripe
from decimal import Decimal

from orders.models import Order

# create the Stripe instance.
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

# Create your views here.


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(klass=Order, id=order_id)

    if request.method == 'POST':
        if 'submit_action' in request.POST:
            action = request.POST['submit_action']

            if action.lower() == 'pay with card':
                success_url = request.build_absolute_uri(
                    reverse('payment:completed'))
                cancel_url = request.build_absolute_uri(
                    reverse('payment:canceled'))

                # stripe checkout session data
                session_data = {
                    'mode': 'payment',
                    'client_reference_id': order.id,
                    'success_url': success_url,
                    'cancel_url': cancel_url,
                    'line_items': []
                }

                # add order items to the stripe checkout session
                for item in order.items.all():
                    session_data['line_items'].append({
                        'price_data': {
                            'unit_amount': int(item.price * Decimal('100')),
                            'currency': 'usd',
                            'product_data': {
                                'name': item.product.name,
                            },
                        },
                        'quantity': item.quantity,
                    })

                # stripe coupon
                if order.coupon:
                    stripe_coupon = stripe.Coupon.create(
                        name=order.coupon.code,
                        percent_off=order.discount,
                        duration='once'
                    )
                    session_data['discounts'] = [{
                        'coupon': stripe_coupon.id
                    }]

                # create Stripe checkout session
                session = stripe.checkout.Session.create(**session_data)

                # redirect to Stripe payment form
                return redirect(to=session.url, code=303)

            elif action.lower() == 'pay with momo':
                return HttpResponse('working on it')

    else:
        return render(request=request, template_name='payment/process.html', context=locals())


def payment_completed(request):
    return render(request=request, template_name='payment/completed.html')


def payment_canceled(request):
    return render(request=request, template_name='payment/canceled.html')
