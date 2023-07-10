from django.db import models

from shortener.views import generate_short_code

class ShortURL(models.Model):
    url = models.CharField(max_length=200)
    short_code = models.CharField(max_length=6, default=generate_short_code, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url