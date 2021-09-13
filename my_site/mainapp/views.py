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
        cart = Cart.get_object(CustomUser.objects.get(id=1))  #request.user
        with transaction.atomic():
            order = Order.get_order(cart)
            amount = request.POST.get("amount")
            kwargs["amount"] = amount
            print(kwargs)
            order.add_product(**kwargs)

        return HttpResponse('all good')


class CartListView(DetailView):
    model = Order
    template_name = 'base.html'
    context_object_name = 'order'
    context_order_products_name = 'order_products'
    pk_url_kwarg = 'order_id'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if not pk:
            cart = Cart.get_object(CustomUser.objects.get(id=1))
            return self.model.get_order(cart)
        return self.model.objects.get(id=pk)

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context[self.context_object_name] = self.object
            context[self.context_order_products_name] = CartProduct.objects.filter(order=self.object)
        context.update(kwargs)
        return super().get_context_data(**context)


# class RemoveFromCart(View):
#
#     def post(self, request, *args, **kwargs):
#
