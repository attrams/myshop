from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    messgae = f'''
    Dear {order.first_name}
    
    You have successfully placed an order. Your order ID is {order.id}.
    '''
    mail_sent = send_mail(
        subject=subject,
        message=messgae,
        from_email='admin@myshop.com',
        recipient_list=[order.email]
    )

    return mail_sent
