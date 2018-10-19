from django.forms import ModelForm

from coins.models import Coin


class CountCoinForm(ModelForm):
    class Meta:
        model = Coin
        fields = ['image']
