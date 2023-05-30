from django.shortcuts import render
from catalog.models import Product, Blog
from django.views import generic


# Create your views here.
def take_homepage(request):
    return render(request, 'catalog/take_homepage.html')


def take_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'пользователь {name} , телефон {phone}, говорит {message}')

    return render(request, 'catalog/take_contact.html')


class ProductListView(generic.ListView):
    model = Product


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):  # выводит только активные записи
        queryset = super().get_queryset()
        queryset = queryset.filter(active_of_publication=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog
