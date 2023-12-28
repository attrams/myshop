from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from cart.forms import CartAddProductForm
from .recommender import Recommender
# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(klass=Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request=request,
        template_name='shop/product/list.html',
        context={
            'category': category,
            'categories': categories,
            'products': products,
        }
    )


def product_detail(request, id, slug):
    product = get_object_or_404(
        klass=Product,
        id=id,
        slug=slug,
        available=True
    )
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(
        request=request,
        template_name='shop/product/detail.html',
        context={'product': product, 'cart_product_form': cart_product_form,
                 'recommended_products': recommended_products}
    )
