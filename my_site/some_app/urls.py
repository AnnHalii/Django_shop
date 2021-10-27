from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('click/', RegisterClickView.as_view(), name='click'),
]