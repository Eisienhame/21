from django.urls import path
from catalog.views import take_contact, take_homepage, ProductListView, BlogListView, BlogCreateView, BlogDetailView
from catalog.views import BlogUpdateView, BlogDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [

    path('', take_homepage, name='homepage'),
    path('take_contact/', take_contact, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='products'),
    path('blog_list/', BlogListView.as_view(), name='blog'),
    path('blog_list/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_list/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_list/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]
