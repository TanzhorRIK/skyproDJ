from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ContactsListView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, \
    ProductDetailView
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('contacts/', ContactsListView.as_view(), name="contacts"),
    path('card/<int:pk>', ProductDetailView.as_view(), name="card"),
    path('blog/create/', BlogCreateView.as_view(), name="add_blog"),
    path('blogs/', BlogListView.as_view(), name="blogs"),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name="blog"),
    path('blog/update/<slug:slug>/', BlogUpdateView.as_view(), name="update_blog"),
    path('blog/delete/<slug:slug>/', BlogDeleteView.as_view(), name="delete_blog")
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)