import requests
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup as Bs
from django.db import IntegrityError
from django.utils.text import Truncator
import datetime
from finance_app.models import Headline


def scrape():
    time = datetime.datetime.now()
    print(f'Scraping from Yahoo {time.time()}')
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
            print(f"Headline created from Yahoo: {new_head.title}")

        except ValidationError:
            continue

        except IntegrityError:
            continue

        except AttributeError:
            continue

        except IndexError:
            continue


def scrape_wsj():
    time = datetime.datetime.now()
    print(f'Scraping from WSJ {time.time()}')
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.wsj.com/news/business?mod=hp_lista_strap"
    soup = Bs(session.get(url, verify=False).content, "html.parser")
    cadru_news1 = soup.find_all("article",
                                {"class": "WSJTheme--story--XB4V2mLz WSJTheme--story-padding--1gRL3tuf WSJTheme-"
                                          "-border-bottom--s4hYCt0s"})
    cadru_news2 = soup.find_all("article", {
        "class": "WSJTheme--story--XB4V2mLz WSJTheme--story-padding--1gRL3tuf WSJTheme--media-margin-bottom--1bIRFuDR"
                 " WSJTheme--border-bottom--s4hYCt0s"})

    for article in cadru_news1[1:]:
        try:
            title = article.find("h3").text
            paragraph = article.find("p").text
            url = article.find("a").get("href")
            img = article.find("img").get("src")

            new_head_wsj1 = Headline()
            new_head_wsj1.title = title
            new_head_wsj1.start_paragraph = paragraph
            new_head_wsj1.start_paragraph = Truncator(new_head_wsj1.start_paragraph).chars(800)
            new_head_wsj1.start_paragraph = "".join(new_head_wsj1.start_paragraph.rsplit(".")[:-1]) + "."

            new_head_wsj1.url = url
            new_head_wsj1.head_img = img

            new_head_wsj1.save()
            print(f"Headline created from WSJ: {new_head_wsj1.title}")

        except ValidationError:
            continue

        except IntegrityError:
            continue

        except AttributeError:
            continue

        except IndexError:
            continue

    for article2 in cadru_news2:
        try:
            title2 = article2.find("h3").text
            paragraph2 = article2.find("p").text
            url2 = article2.find("a").get("href")
            img2 = article2.find("img").get("src")

            new_head_wsj2 = Headline()
            new_head_wsj2.title = title2
            new_head_wsj2.start_paragraph = paragraph2
            new_head_wsj2.start_paragraph = Truncator(new_head_wsj2.start_paragraph).chars(800)
            new_head_wsj2.start_paragraph = "".join(new_head_wsj2.start_paragraph.rsplit(".")[:-1]) + "."
            new_head_wsj2.url = url2
            new_head_wsj2.head_img = img2

            new_head_wsj2.save()
            print(f"Headline created from WSJ: {new_head_wsj2.title}")

        except ValidationError:
            continue

        except IntegrityError:
            continue

        except AttributeError:
            continue

        except IndexError:
            continue
