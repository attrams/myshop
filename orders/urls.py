from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path(route='create/', view=views.order_create, name='order_create'),
]
