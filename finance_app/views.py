import requests
from django.shortcuts import render, redirect
from finance_app import scraper
from finance_app.models import Headline
from apscheduler.schedulers.background import BackgroundScheduler

from finance_app.scraper import scrape

requests.packages.urllib3.disable_warnings()


def scraper_view(request):
    scraper.scrape()

    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape, 'interval', minutes=10)
    scheduler.start()

    return redirect("../")


def article_list(request):
    articles = Headline.objects.all()[::-1]
    lista = {"object_list": articles}
    return render(request, "../index.html", lista)
