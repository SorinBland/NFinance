from django.urls import path, include

from finance_app.views import article_list, scraper_view, ticker_list

urlpatterns = [
    path("scraper/", scraper_view, name="scraper"),
    path("", article_list, name="index"),
    path("tickers/", ticker_list, name="tickers"),

]
