from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'coins/upload_image_form.html')


def upload(request):
    return HttpResponse(1)
