from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.DO_NOTHING)#добавить on_delete=models.PROTECT
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество')
    characteristics = models.JSONField(verbose_name='Характеристики')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        ordering = ['id', 'title']


class CartProduct(models.Model):

    order = models.ForeignKey('Order', verbose_name='Корзина', on_delete=models.CASCADE, related_name='cart_product')
    chosen_product = models.ForeignKey(Product, verbose_name='Выбраный продукт', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Продукт {self.chosen_product.title} (для корзины)'

    class Meta:
        verbose_name = 'Корзина товара'
        verbose_name_plural = 'Корзины товаров'


class Order(models.Model):
    DEFAULT = 'new'
    ORDER_STATUSES = [
        ('new', 'Новый'),
        ('confirmed', 'Подтверждён'),
        ('rejected', 'Отклонён'),
        ('ordered', 'Доставлен'),
        ('payed', 'Оплачен'),
    ]
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='order')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
    order_status = models.CharField(max_length=15, choices=ORDER_STATUSES, default=DEFAULT)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Cart(models.Model):

    owner = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
