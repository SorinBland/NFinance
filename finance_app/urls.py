from django.urls import path
from finance_app.views import article_list, scraper_view, ticker_list, filter_news, crypto

urlpatterns = [
    path("scraper/", scraper_view, name="scraper"),
    path("", article_list, name="index"),
    path("filter/", filter_news, name='filter'),
    path("tickers/", ticker_list, name="tickers"),
    path("crypto/", crypto, name='crypto'),

]
