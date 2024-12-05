from django.urls import path
from .views import *

urlpatterns = [
    path('', platform_view, name='platform'),
    path('store/', games_view, name='games'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<slug:item_id>/', add_to_cart, name='add_to_cart'),
    path('django_sign_up/', sign_up_by_django, name='signup-django'),
]