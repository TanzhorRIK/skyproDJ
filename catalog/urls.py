from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts
from config import settings

urlpatterns = [
    path('', index),
    path('contacts/', contacts)
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)