from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        object_1 = Category.objects.get(id=7, name='Веб-камеры')

        products_list = [
            {'name': 'Китай', 'description': 'БУ',
             'preview': 'media/photos/2023/07/25/i.webp', 'category': object_1, 'price': 1000.0},
        ]

        Product.objects.all().delete()

        products_for_create = []

        for product in products_list:
            products_for_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_for_create)