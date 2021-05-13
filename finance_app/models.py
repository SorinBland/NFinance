from django.db import models
from django.utils import timezone


class Headline(models.Model):
    title = models.CharField(max_length=100, unique=True)
    datetime = models.DateTimeField(default=timezone.now)
    head_img = models.URLField(unique=True)
    start_paragraph = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return f"{self.title}, {self.start_paragraph}"


class Ticker(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    current_price = models.CharField(max_length=30, blank=True, null=False)
    previous_close = models.CharField(max_length=30, blank=True, null=True)
    open = models.CharField(max_length=30, blank=True, null=True)
    bid = models.CharField(max_length=30, blank=True, null=True)
    ask = models.CharField(max_length=30, blank=True, null=True)
    volume = models.CharField(max_length=30, blank=True, null=True)
    avg_volume = models.CharField(max_length=30, blank=True, null=True)
    market_cap = models.CharField(max_length=30, blank=True, null=True)
    earnings_date = models.CharField(max_length=30, blank=True, null=True)
    year_target_est = models.CharField(max_length=30, blank=True, null=True)
    year_range = models.CharField(max_length=30, blank=True, null=True)
    day_range = models.CharField(max_length=30, blank=True, null=True)
    tick = models.CharField(max_length=10, blank=True, null=True)
    company_profile = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

