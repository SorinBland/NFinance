import requests
from django.shortcuts import render, redirect
from finance_app.models import Headline, Ticker
from apscheduler.schedulers.background import BackgroundScheduler
from finance_app.scraper import scrape
from finance_app.scraper_tickers import scrape_ticker

requests.packages.urllib3.disable_warnings()


# rezultatul care apare dupa introducerea inputului
def ticker_list(request):
    Ticker.objects.all().delete()
    ticker = request.POST.get('ticker')
    scrape_ticker(ticker)
    graph_url = f'https://www.tradingview.com/symbols/{ticker}/'
    ticker_info = Ticker.objects.all()
    context = {"ticker_list": ticker_info, 'graph_url': graph_url}
    return render(request, "tickers.html", context)


def scraper_view(request):
    scrape()

    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape, 'interval', minutes=10)
    scheduler.start()

    return redirect("../")


def article_list(request):
    articles = Headline.objects.all()[::-1]
    lista = {"object_list": articles}

    return render(request, "index.html", lista)
