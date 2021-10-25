from rest_framework import serializers
from mainapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'characteristics', 'price')
