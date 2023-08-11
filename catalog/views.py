from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, \
    DetailView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = "cards"
    extra_context = {"title": "Главная страница"}


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/card.html'


class ProductCreate(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'price', 'category')
    success_url = reverse_lazy('catalog:product_list')


class ContactsListView(ListView):
    model = Product
    template_name = 'main/contacts.html'
    extra_context = {'title': "Контакты"}


class BlogListView(ListView):
    model = Blog
    template_name = 'main/blog_list.html'
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
    template_name = 'main/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        blog = Blog.objects.get(pk=self.object.pk)
        blog.count_views += 1
        blog.save()
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'main/blog_form.html'
    extra_context = {
        'title': 'Добавить пост'
    }
    fields = ('name', 'content', 'preview', 'publication_attribute',)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        return context


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'main/blog_update.html'
    fields = ('name', 'content', 'preview', 'publication_attribute',)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context
