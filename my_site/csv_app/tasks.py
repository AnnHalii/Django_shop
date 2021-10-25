from my_site.celery import app
from mainapp.models import Product
import csv


@app.task
def generate_csv():
    with open('productssss.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['category', 'title', 'price', 'manufacturer'])
        products = Product.objects.all().values_list('category', 'title', 'price', 'manufacturer')
        for product in products:
            writer.writerow(product)
