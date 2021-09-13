from rest_framework import viewsets, generics
from .serializers import ProductSerializer
from mainapp.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
