from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path(route='process/', view=views.payment_process, name='process'),
    path(route='completed/', view=views.payment_completed, name='completed'),
    path(route='canceled/', view=views.payment_canceled, name='canceled'),
]
