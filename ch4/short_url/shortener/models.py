import string
import random

from django.db import models

class ShortURL(models.Model):
    code = models.CharField(max_length=8, unique=True)
    original_url = models.URLField(max_length=200)
    access_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # {app_label}_{클래스명 소문자}
    # db table: shortener_shorturl
    class Meta:
        app_label = 'shortener'
        db_table = 'short_url'

    @staticmethod
    def generate_code():
        characters = string.ascii_letters + string.digits
        return "".join(random.choices(characters, k=8))