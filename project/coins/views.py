from django.views.generic import CreateView
from coins.models import Coin

from coins import utils


class CoinCreate(CreateView):
    model = Coin
    fields = ['image']
    success_url = '/'

    def get(self, request, *args, **kwargs):
        self.request.image_info = self.request.session.pop('image_info', None)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        coin = form.save()
        opened_img = utils.open_image(coin.image.path)
        width, height = utils.get_metadata(opened_img)
        red, green, blue = utils.get_average_color(opened_img)
        image_info = {
            'width': width,
            'height': height,
            'red': red,
            'green': green,
            'blue': blue,
            'number_of_coins': utils.count_coins(coin.image.path)
        }
        self.request.session['image_info'] = image_info
        return super().form_valid(form)


