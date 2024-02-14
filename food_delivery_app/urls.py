# food_delivery_app/urls.py

from django.urls import path
from .views import calculate_price, default_view

urlpatterns = [
    path('calculate_price/', calculate_price, name='calculate_price'),
    path('', default_view, name='default'),
]
