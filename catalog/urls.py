from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, card
from config import settings

urlpatterns = [
    path('', index, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('card/', card, name="card")
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)