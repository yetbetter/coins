from django.contrib import messages
from django.core.files.images import get_image_dimensions
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, FormView

from coins.models import Coin


# def home(request):
#     return render(request, 'coins/upload_image_form.html')
#
#
# def upload(request):
#     images = request.FILES.getlist('images')
#
#     for image in images:
#         print(get_image_dimensions(image))
#     return HttpResponse(images)

from coins.forms import CountCoinForm


# class CoinList(ListView):
#     model = Coin
#
#
# class CoinCreate(CreateView):
#     model = Coin
#     fields = ['image']
#     success_url = '/'


class CountCoinView(FormView):
    template_name = 'coins/coin_count.html'
    form_class = CountCoinForm
    success_url = '/'

    def form_valid(self, form):
        # image = self.request.FILES.get('image')
        # print(get_image_dimensions(image))
        messages.add_message(self.request, messages, 'hi')
        return super().form_valid(form)

