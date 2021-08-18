from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    # path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]
