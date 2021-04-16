from django.db import models


# Create your models here.
from django.utils import timezone


class Headline(models.Model):
    title = models.CharField(max_length=100, unique=True)
    datetime = models.DateTimeField(default=timezone.now) #scrape time here and display
    head_img = models.URLField(unique=True)
    start_paragraph = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return f"{self.title}, {self.start_paragraph}"


class Ticker(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    current_price = models.CharField(max_length=30, blank=True, null=False)
    previous_close = models.CharField(max_length=30, blank=True, null=False)
    open = models.CharField(max_length=30, blank=True, null=False)
    bid = models.CharField(max_length=30, blank=True, null=False)
    ask = models.CharField(max_length=30, blank=True, null=False)
    volume = models.CharField(max_length=30, blank=True, null=False)
    avg_volume = models.CharField(max_length=30, blank=True, null=False)
    market_cap = models.CharField(max_length=30, blank=True, null=False)
    earnings_date = models.CharField(max_length=30, blank=True, null=False)
    year_target_est = models.CharField(max_length=30, blank=True, null=False)
    year_range = models.CharField(max_length=30, blank=True, null=False)
    day_range = models.CharField(max_length=30, blank=True, null=False)
    tick = models.CharField(max_length=10, blank=True, null=True)
    company_profile = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

