from django.urls import path

from coins.views import CountCoinView

urlpatterns = [
    # path('', CoinList.as_view(), name='coin-list'),
    # path('coin/create', CoinCreate.as_view(), name='coin-create'),
    path('', CountCoinView.as_view(), name='coin-count')
]