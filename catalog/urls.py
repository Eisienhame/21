from django.urls import path
from catalog.views import take_contact, take_homepage, ProductListView, test
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [

    path('', take_homepage, name='homepage'),
    path('take_contact/', take_contact, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='products'),
    path('test/', test, name='test'),

]
