from django.urls import path
from finance_app.views import article_list, scraper_view

urlpatterns = [
    path("scraper/", scraper_view, name="scraper"),
    path("", article_list, name="index"),
]