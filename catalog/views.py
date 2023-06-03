from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Blog
from django.views import generic
from django.urls import reverse_lazy


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        get_object_or_404(Blog, pk=self.get_object().pk).increase_views()
        return context_data


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('article_title', 'slug', 'content', 'preview_image')
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('article_title', 'slug', 'content', 'preview_image')
    success_url = reverse_lazy('catalog:blog_list')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
