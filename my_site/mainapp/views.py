from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def test_view(request):
    return render(request, 'base.html', {})


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
