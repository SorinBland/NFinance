from django.urls import path
from finance_app.views import scraper, article_list

urlpatterns = [
    path("scraper/", scraper, name="scraper"),
    path("", article_list, name="index"),
]