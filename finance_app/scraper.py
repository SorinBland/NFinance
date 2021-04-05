import requests
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup as Bs
from django.db import IntegrityError
from django.utils.text import Truncator
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Finance_news_aggregator.settings'
django.setup()

from finance_app.models import Headline


def scrape():
    print('Scraping')
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://finance.yahoo.com"
    content = session.get(url, verify=False).content
    soup = Bs(content, "html.parser")
    cadru_mare = soup.find_all("div", "Cf")

    for article in cadru_mare[3:]:
        try:
            titlu = article.find("a").text
            paragraf = article.find("p").text
            url = article.find("a").get("href")
            img = article.find("img").get("src")

            new_head = Headline()
            new_head.title = titlu
            new_head.head_img = img
            new_head.url = f"https://finance.yahoo.com/{url}"
            new_head.start_paragraph = paragraf

            new_head.start_paragraph = Truncator(new_head.start_paragraph).chars(800)
            new_head.save()

        except ValidationError:
            continue

        except IntegrityError:
            continue

        except AttributeError:
            continue

        except IndexError:
            continue
