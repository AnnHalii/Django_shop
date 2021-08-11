from django.shortcuts import render
from .models import *


def test_view(request):
    return render(request, 'base.html', {})

#
# class ProductDetailView(DetailView):
#
#     CT_MODEL_MODEL_CLASS = {
#         'notebook': Notebook,
#         'smartphone': Smartphone
#     }
#
    # def dispatch(self, request, *args, **kwargs):
    #     self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
    #     self.queryset = self.model._base_manager.all()
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     print('kdkdkdkd')
    #     pass
    #
    # # model = Model
    # # queryset = Model.objects
    # context_object_name = 'product'
    # template_name = 'product_detail.html'
    # slug_url_kwarg = 'slug'
