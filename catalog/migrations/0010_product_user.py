# Generated by Django 4.2.1 on 2023-06-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Создатель'),
        ),
    ]
