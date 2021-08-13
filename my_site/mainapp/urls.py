from django.urls import path
from .views import *
from .views import test_view


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    # path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]
