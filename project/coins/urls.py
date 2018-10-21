from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from coins.views import CoinCreate

urlpatterns = [
    path('', CoinCreate.as_view(), name='coin-create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
