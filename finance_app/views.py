import requests
from django.shortcuts import render, redirect
from finance_app.models import Headline, Ticker
from apscheduler.schedulers.background import BackgroundScheduler
from finance_app.scraper import scrape
from finance_app.scraper_tickers import scrape_ticker

requests.packages.urllib3.disable_warnings()


def scraper_ticker_view(request):
    scrape_ticker()

    return redirect(ticker_list)


def ticker_list(request):
    ticker_info = Ticker.objects.all()
    lista = {"ticker_list": ticker_info}

    return render(request, "tickers.html", lista)


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
