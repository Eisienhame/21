from django.urls import path
from catalog.views import take_contact, take_homepage, ProductListView, BlogListView, BlogCreateView, BlogDetailView
from catalog.views import BlogUpdateView, BlogDeleteView, ProductDeleteView, ProductCreateView, ProductDetailView, ProductUpdateView
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [

    path('', take_homepage, name='homepage'),
    path('take_contact/', take_contact, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/create/', ProductCreateView.as_view(), name='product_create'),
    path('product_list/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_list/<int:pk>/',cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_list/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_list/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_list/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_list/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),


]
