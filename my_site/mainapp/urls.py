from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
    path('cart/product/<slug:product_slug>/', AddToCartView.as_view(), name='add_to_cart'),
]
