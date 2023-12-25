from django.shortcuts import render

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

            order_created.delay(order.id)

            return render(request=request, template_name='orders/order/created.html', context={'order': order})

    else:
        form = OrderCreateForm()

    return render(request=request, template_name='orders/order/create.html', context={'cart': cart, 'form': form})