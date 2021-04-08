from django.contrib import admin
from .models import Headline, Ticker

# Register your models here.

admin.site.register(Headline)
admin.site.register(Ticker)