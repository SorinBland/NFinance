import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from finance_app.models import Headline, Ticker
from finance_app.scraper import scrape, scrape_wsj
from finance_app.scraper_tickers import scrape_ticker


requests.packages.urllib3.disable_warnings()


# Ticker info after user input is entered
def ticker_list(request):
    try:
        Ticker.objects.all().delete()
        ticker = request.POST.get('ticker')
        scrape_ticker(ticker)
        graph_url = f'https://www.tradingview.com/symbols/{ticker}/'
        ticker_info = Ticker.objects.all()
        context = {"ticker_list": ticker_info, 'graph_url': graph_url}
        return render(request, "tickers.html", context)
    except ImportError:
        return HttpResponse("There are no tickers matching your search, please try again.")


# Scraper method called every 10 minutes by BackgroundScheduler
def scraper_view(request):
    scrape()
    scrape_wsj()
    return redirect("../")


# Articles that appear on the front page after being scraped
def article_list(request):
    articles = Headline.objects.all()[::-1]
    context = {"object_list": articles}

    return render(request, "index.html", context)


# Search method
def filter_news(request):
    filter_term = request.POST.get('filter')
    articles_filtered = Headline.objects.filter(title__icontains=f"{filter_term}")
    if articles_filtered:
        context = {'articles_filtered': articles_filtered}
        return render(request, "filter.html", context)
    else:
        return HttpResponse("There are no news matching your search, please try again.")


# Filter for crypto page
def crypto(request):
    crypto_news = Headline.objects.filter(title__icontains="crypto") | \
                  Headline.objects.filter(title__icontains="bitcoin") | \
                  Headline.objects.filter(title__icontains="ethereum") | \
                  Headline.objects.filter(title__icontains="coin") | \
                  Headline.objects.filter(title__icontains='cryptos') | \
                  Headline.objects.filter(title__icontains='altcoin')

    context = {'crypto_news': crypto_news[::-1]}

    return render(request, 'crypto.html', context)
