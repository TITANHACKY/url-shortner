import short_url as short_url
from django.db import models

class ShortUrl(models.Model):
    url = models.URLField(null=False)
    short_code = models.CharField(max_length=10, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_code