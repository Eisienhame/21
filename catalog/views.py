from django.shortcuts import render, get_object_or_404
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version
from django.views import generic
from django.urls import reverse_lazy
# from django.conf import settings
# from django.core.cache import cache


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


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Product
    permission_required = 'catalog.view_product'


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'preview_image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Product

    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    #fields = ('name', 'description', 'preview_image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class BlogListView(LoginRequiredMixin, generic.ListView):
    model = Blog

    def get_queryset(self):  # выводит только активные записи
        queryset = super().get_queryset()
        queryset = queryset.filter(active_of_publication=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        get_object_or_404(Blog, pk=self.get_object().pk).increase_views()
        return context_data


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ('article_title', 'slug', 'content', 'preview_image')
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    fields = ('article_title', 'slug', 'content', 'preview_image')
    success_url = reverse_lazy('catalog:blog_list')


    # def success_url(self, *args, **kwargs):
    #     return reverse_lazy('catalog:blog_update', args=[self.get_object().pk])


class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
