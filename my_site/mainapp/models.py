from django.db import models
from django.conf import settings


class LatestProductsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('-id')[:5]


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество')
    characteristics = models.JSONField(verbose_name='Характеристики')
    # latest_products = LatestProductsManager()

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name='Продукты'
    #     verbose_name_plural='Продукты'
    #     ordering=['title', 'id']


class CartProduct(models.Model):

    order = models.ForeignKey('Order', verbose_name='Корзина', on_delete=models.CASCADE, related_name='cart_product')
    chosen_product = models.ForeignKey(Product, verbose_name='Выбраный продукт', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Продукт {self.chosen_product.title} (для корзины)'


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


class Cart(models.Model):

    owner = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.id)
