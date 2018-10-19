from django.urls import path

from coins import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload_image')
]