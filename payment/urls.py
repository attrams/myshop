from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'payment'

urlpatterns = [
    path(route=_('process/'), view=views.payment_process, name='process'),
    path(route=_('completed/'), view=views.payment_completed, name='completed'),
    path(route=_('canceled/'), view=views.payment_canceled, name='canceled'),
]
