from django.views.generic import ListView, DetailView, CreateView
from .models import *


class ProductListView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'base.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product_detail'


# def show_category(request, cat_id):
#     return HttpResponse(f"Отображение продукта с номером: {cat_id}")

