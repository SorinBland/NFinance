from django.urls import path


from finance_app.views import article_list, scraper_view, scraper_ticker_view, ticker_list

urlpatterns = [
    path("scraper/", scraper_view, name="scraper"),
    path("", article_list, name="index"),
    path("tickers/", ticker_list, name="tickers"),
    path('tick/', scraper_ticker_view, name='tick')
]
