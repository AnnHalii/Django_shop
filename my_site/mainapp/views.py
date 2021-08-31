from django.db import transaction
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import *
from user_app.models import CustomUser


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


class AddToCartView(View):

    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        cart = Cart.get_object(CustomUser.objects.get(id=1))  #request.user
        with transaction.atomic():
            order = Order.get_order(cart)
            amount = request.POST.get("amount")
            kwargs["amount"] = amount
            print(kwargs)
            order.add_product(**kwargs)

        return HttpResponse('all good')
