from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'price', 'amount')
    list_display_links = ('title', 'image', 'amount')
    search_fields = ('title', 'description')
    list_filter = ('title', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
