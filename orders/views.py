from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

# Create your views here.


def order_create(request):
    cart = Cart(request=request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(to=reverse('payment:process'))

    else:
        form = OrderCreateForm()

    return render(request=request, template_name='orders/order/create.html', context={'cart': cart, 'form': form})
