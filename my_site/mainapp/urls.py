from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='product_detail')
]
