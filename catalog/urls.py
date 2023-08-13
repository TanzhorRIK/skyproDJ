from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ContactsListView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, \
    ProductDetailView, VersionCreateView, ProductCreateView
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('contacts/', ContactsListView.as_view(), name="contacts"),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('card/<int:pk>', ProductDetailView.as_view(), name="card"),
    path('add_blog/', BlogCreateView.as_view(), name="add_blog"),
    path('blogs/', BlogListView.as_view(), name="blogs"),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name="blog"),
    path('blog/update/<slug:slug>/', BlogUpdateView.as_view(), name="update_blog"),
    path('blog/delete/<slug:slug>/', BlogDeleteView.as_view(), name="delete_blog"),
    path('version/', VersionCreateView.as_view(), name='add_version')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)