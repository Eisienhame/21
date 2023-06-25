from django.core.management import BaseCommand
from django.utils import timezone
from catalog.models import Category, Product, Version, Blog
import datetime
import psycopg2, os

class Command(BaseCommand):
    def handle(self, *args, **options):
        with psycopg2.connect(
                host="localhost",
                database="lesson20",
                user="postgres",
                password=os.getenv('bd_pass')) as conn:
            with conn.cursor() as cur:
                cur.execute('truncate table catalog_product, catalog_category, catalog_version, catalog_blog')
                #cur.execute('ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1')

        categories_list = [
            {"name": "fruits", "description": "Фрукты"},
            {"name": "Sweet", "description": "Сладкое"},
            {"name": "Vegetables", "description": "Овощи"},
            {"name": "Telephones", "description": "Телефоны и планшеты"},
            {"name": "Meat", "description": "Мясо"}
        ]
        category_objects = []
        for i in categories_list:
            category_objects.append(Category(**i))

        Category.objects.bulk_create(category_objects)


        product_list = [
            {"name": "mango", "description": "fruits", "preview_image": "products/freshmango.jpg", "price": "124","date_of_creation": f"{datetime.datetime.now()}","Last_modified_date": f"{datetime.datetime.now()}"},
            {"name": "banan", "description": "fruits", "preview_image": "products/01banan.jpg", "price": "32","date_of_creation": f"{datetime.datetime.now()}","Last_modified_date": f"{datetime.datetime.now()}"},
            {"name": "Яблоко", "description": "fruits", "preview_image": "products/03яблоко.jpg", "price": "14","date_of_creation": f"{datetime.datetime.now()}","Last_modified_date": f"{datetime.datetime.now()}"}
        ]
        product_objects = []
        for i in product_list:
            product_objects.append(Product(**i))

        Product.objects.bulk_create(product_objects)


        # version_list = [
        #     {"product_name": "банан", "number_ver": 1, "name_ver": "totti", "flag_ver": "fruits", "product": banan}
        # ]
        #
        # version_objects = []
        # for i in version_list:
        #     version_objects.append(Version(**i))
        #
        # Version.objects.bulk_create(version_objects)

        blog_list = [
            {"article_title": "Test", "slug": "test", "content": "TEST", "date_of_creation": f"{datetime.datetime.now()}", "active_of_publication": True, 'views_count': 0}
        ]

        blog_objects = []
        for i in blog_list:
            blog_objects.append(Blog(**i))

        Blog.objects.bulk_create(blog_objects)