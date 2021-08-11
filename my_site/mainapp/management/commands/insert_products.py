import random
from string import ascii_lowercase
from os import listdir
from os.path import isfile, join

from django.core.management.base import BaseCommand
from mainapp.models import Product, Category


class Command(BaseCommand):
    help = 'Creates new records in the database'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of created records')

    def handle(self, *args, **options):
        products = []
        categories = Category.objects.all()
        image_files = [f for f in listdir("script_db_images") if isfile(join("script_db_images", f))]
        for _ in range(options['total']):
            products.append(Product(
                category=random.choice(categories),
                title=random.choice(['Iphone 12 64Gb Purple', 'IPhone 11 64Gb White',
                                     'Apple Watch Series 6 GPS 40mm Gold Aluminum Case with Pink Sand Sport Band (MG123)']),
                slug=''.join(random.choice(ascii_lowercase) for i in range(6)),
                image=random.choice(image_files),
                description=random.choice([
                    'Тим Кук и его команда создали красивый iPhone 12, который своим более угловатым дизайном вдохновляет iPhone 5. Apple представила модель с 6,1-дюймовым экраном Super Retina XDR до самых краев.',
                    'iPhone 11 сравнительно недорогой флагман, в котором представлены все новые технологии линейки. Эта модель, по сути, является преемником iPhone XR, с некоторыми новшествами и нововведениями. Кому-то они кажутся даже более интересными, чем у более дорогих моделей. Apple не вносила революционных решений и функций в iPhone 11, но его функционал был усовершенствован настолько грамотно, что именно эта модель имеет все шансы стать самой популярной и любимой у пользователей.',
                    'Apple Watch, несомненно, были самыми успешными умными часами на рынке в течение нескольких лет. Некоторые производители пытаются имитировать часы Apple своей продукцией, но тщетно. Умные часы Apple Watch Series 6 - элегантный и полезный спутник, который будет сопровождать вас повсюду. Собираетесь ли вы на футбольное поле или на вечеринку, Apple Watch Series 6 станет для вас отличным дополнением. Благодаря новым функциям здоровый образ жизни становится действительно легкой задачей.']),
                price=random.choice([23630, 19040, 12150]),
                manufacturer="Apple",
                amount=1,
                characteristics=random.choice([{"Цвет": "Purple", "Модель": "iPhone 12", "Диагональ": 6.1,
                                                "Процессор": "A14 Bionic", "Год выпуска": 2021, "Объем памяти": "64 GB",
                                                "Оперативная память": "4 GB"},
                                               {"Цвет": "White", "Модель": "iPhone 11", "Диагональ": 6.1,
                                                "Процессор": "A13 Bionic", "Год выпуска": 2019, "Объем памяти": "64 GB",
                                                "Оперативная память": "4 GB"},
                                               {"Цвет": "Gold", "Модель": "Apple Watch Series 6 40mm", "Размер": "40mm",
                                                "Процессор": "Apple S6", "Год выпуска": 2020, "Объем памяти": "32 GB"}])

            ))
        Product.objects.bulk_create(products)
