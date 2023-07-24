from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Веб-камеры',
             'description': 'камеры'},
            {'name': 'Компьютеры',
             'description': 'Ноутбуки'},
            {'name': 'Компьютеры',
             'description': 'Стационарные'}
        ]



        categories_for_create = []

        for categories in category_list:
            categories_for_create.append(
                Category(**categories)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)


