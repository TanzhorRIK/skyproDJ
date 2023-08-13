from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, \
    DetailView

from catalog.forms import BlogForm, ProductForm, VersionForm
from catalog.models import Product, Blog, Version


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = "cards"
    extra_context = {"title": "Главная страница"}


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/card.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'preview', 'price', 'category')
    success_url = reverse_lazy('catalog:home')


class ContactsListView(ListView):
    model = Product
    template_name = 'catalog/contacts.html'
    extra_context = {'title': "Контакты"}


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # template_name = 'catalog/blog_form.html'
    extra_context = {
        'title': 'Добавить пост'
    }
    # fields = ('name', 'content', 'preview', 'publication_attribute',)
    success_url = reverse_lazy('catalog:blogs')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    # template_name = 'catalog/blog_list.html'
    extra_context = {
        'name': 'Блог'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_attribute=True)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        return context


class BlogDetailView(DetailView):
    model = Blog
    # template_name = 'catalog/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        blog = Blog.objects.get(pk=self.object.pk)
        blog.count_views += 1
        blog.save()
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context



class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "catalog/blog_update.html"
    fields = ('name', 'content', 'preview', 'publication_attribute',)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.object.owner = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:index')



