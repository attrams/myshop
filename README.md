# myshop

a simple ecommerce website that allows users to add items to cart, checkout items, browse products
and etc.

## what I learnt

- using django sessions to store cart items.
- creating custom context processors.
- using [celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) and [rabbitmq](https://www.rabbitmq.com/#getstarted) to create asynchronous task(sending email when order is completed).

## Project Screenshots

All product images are from [unsplash](https://unsplash.com/)

![product list page](assets/img/product_list_page.png)
![product detail page](assets/img/product_detail_page.png)
![empty cart](assets/img/empty_cart.png)
![cart items](assets/img/cart_items.png)
![order checkout](assets/img/order_checkout.png)
![order completed](assets/img/order_completed.png)

## libraries used

- [pillow](https://python-pillow.org/) - required since image field is used in the product model.
- [celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) - for sending email asynchronously when order is created.
- [flower]() - for monitoring asynchronous task instead of using rabbitmq management ui.

## PS

- [celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) requires a message broker. You can check this part of
  the [documentation](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#choosing-a-broker) on how to install one.
