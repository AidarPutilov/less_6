from django.core.management import BaseCommand
from catalog.models import Product, Category
import json

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         student_list = [
#             {'last_name': 'Панина', 'first_name': 'Александра'},
#             {'last_name': 'Жуков', 'first_name': 'Даниил'},
#             {'last_name': 'Григорьев', 'first_name': 'Леонид'},
#             {'last_name': 'Завьялова', 'first_name': 'Варвара'},
#             {'last_name': 'Козлова', 'first_name': 'Вера'},
#             {'last_name': 'Емельянова', 'first_name': 'Виктория'},
#             {'last_name': 'Болдырев', 'first_name': 'Глеб'},
#             {'last_name': 'Малинин', 'first_name': 'Антон'},
#             {'last_name': 'Зверева', 'first_name': 'Татьяна'},
#             {'last_name': 'Некрасов', 'first_name': 'Алексей'},
#         ]
#         students_for_create =[]
#         for student_item in student_list:
#             students_for_create.append(
#                 Student(**student_item)
#             )
#         Student.objects.bulk_create(students_for_create)

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        result = []
        with open('data.json', encoding='utf-8') as f:
            for item in json.load(f):
                if item['model'] == 'catalog.category':
                    result.append(item)
        return result

    @staticmethod
    def json_read_products():
        result = []
        with open('data.json', encoding='utf-8') as f:
            for item in json.load(f):
                if item['model'] == 'catalog.product':
                    result.append(item)
        return result

    def handle(self, *args, **options):

        # Очистка таблиц
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание списков для заполнения таблиц
        product_for_create = []
        category_for_create = []

        # Заполнение категорий
        for item in Command.json_read_categories():
            category = {
                'id': item['pk'],
                'name': item['fields']['name'],
                'description': item['fields']['description']
            }
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)

        # Заполнение продуктов
        for item in Command.json_read_products():
            i = {
                'id': item['pk'],
                'name': item['fields']['name'],
                'description': item['fields']['description'],
                'preview': item['fields']['preview'],
                'price': item['fields']['price'],
                'created_at': item['fields']['created_at'],
                'updated_at': item['fields']['updated_at'],
                'category': Category.objects.get(pk=item['fields']['category'])
            }
            product_for_create.append(Product(**i))
        Product.objects.bulk_create(product_for_create)
