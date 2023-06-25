from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=400, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=400, verbose_name='Описание', **NULLABLE)
    preview_image = models.ImageField(upload_to='products/', verbose_name='Изображение (превью)', **NULLABLE)
    #category = models.CharField(max_length=150, verbose_name='Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    Last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)
    user = models.CharField(max_length=150, verbose_name='Создатель', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано', **NULLABLE)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)





class Blog(models.Model):
    article_title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",)
    content = models.TextField(max_length=5000, verbose_name='Содержимое')
    preview_image = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    active_of_publication = models.BooleanField(default=True, verbose_name='Активный')
    views_count = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return f'{self.article_title}'

    def get_absolute_url(self):
        return reverse('record_detail', kwargs={'slug': self.slug})

    def increase_views(self):
        self.views_count += 1
        self.save()

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('article_title',)


class Version(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    number_ver = models.IntegerField(default=0.0, verbose_name='Номер версии')
    name_ver = models.CharField(max_length=150, verbose_name='Наименование версии')
    flag_ver = models.CharField(max_length=150, verbose_name='Признак текущей версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return f'{self.product} {self.number_ver}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

