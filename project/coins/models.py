from django.db import models


class Coin(models.Model):
    image = models.ImageField(upload_to='coins')