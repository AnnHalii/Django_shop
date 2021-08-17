from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class ProductListView(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'products'


def show_product(request, slug_id):
    return HttpResponse(f"Отображение продукта со слагом: {slug_id}")


# def show_category(request, cat_id):
#     return HttpResponse(f"Отображение продукта с номером: {cat_id}")
