# Generated by Django 4.2.1 on 2023-06-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Опубликовано'),
        ),
    ]
