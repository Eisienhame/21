from django.contrib import admin
from catalog.models import Category, Product, Blog, Version
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)

@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'active_of_publication')
    prepopulated_fields = {"slug": ("article_title",)}

@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'number_ver', 'name_ver')
    list_filter = ('name_ver',)

