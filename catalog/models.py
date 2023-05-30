from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=400, verbose_name='Описание', **NULLABLE)
    preview_image = models.ImageField(upload_to='products/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    Last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=400, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Blog(models.Model):
    article_title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(max_length=15000, verbose_name='Содержимое')
    preview_image = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    active_of_publication = models.BooleanField(default=True, verbose_name='Активный')
    views_count = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return f'{self.article_title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('article_title',)
