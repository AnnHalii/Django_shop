from django.forms import ModelChoiceField
from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Cart)
