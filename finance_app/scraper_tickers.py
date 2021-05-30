import requests
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup as Bs
from django.db import IntegrityError
import re
from django.utils.text import Truncator
from finance_app.models import Ticker


requests.packages.urllib3.disable_warnings()


# Ticker scraper file
def scrape_ticker(user_input):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

    # price info tables
    url = f"https://finance.yahoo.com/quote/{user_input}?p={user_input}"
    soup = Bs(session.get(url, verify=False).content, "html.parser")
    cadru_mare = soup.find_all("div", {"id": "quote-summary"})
    cadru_titlu = soup.find_all("div", {"class": "D(ib)"})
    cadru_current_price = soup.find_all("div", {"class": "D(ib) Mend(20px)"})

    # summary
    url = f"https://finance.yahoo.com/quote/{user_input}/profile?p={user_input}"
    soup = Bs(session.get(url, verify=False).content, "html.parser")
    cadru_summary = soup.find_all("p", {"class": "Mt(15px)"})
    new_ticker = Ticker()

    for summary in cadru_summary:
        try:
            ticker_summary = summary.text
            new_ticker.company_profile = ticker_summary
            new_ticker.company_profile = Truncator(new_ticker.company_profile).chars(400)

        except AttributeError:
            continue

    for elem in cadru_titlu:
        try:
            title = elem.find("h1").text
            tick_from_title = re.findall(r'\(.*?\)', title)
            for tick in tick_from_title:
                new_ticker.tick = str(tick).strip("()")
                new_ticker.title = title

        except AttributeError:
            continue

    for price in cadru_current_price:
        try:
            current_price = price.find("span", {"data-reactid": "32"}).text
            new_ticker.current_price = current_price
        except AttributeError:
            continue

    for date in cadru_mare:
        try:
            previous_close = date.find("td", {"data-test": "PREV_CLOSE-value"}).text
            open_price = date.find("td", {"data-test": "OPEN-value"}).text
            bid = date.find("td", {"data-reactid": "53"}).text
            ask = date.find("td", {"data-test": "ASK-value"}).text
            volume = date.find("td", {"data-test": "TD_VOLUME-value"}).text
            avg_volume = date.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text
            market_cap = date.find("td", {"data-test": "MARKET_CAP-value"}).text
            earnings_date = date.find("td", {"data-test": "EARNINGS_DATE-value"}).text
            year_target_est = date.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text
            year_range = date.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text
            day_range = date.find("td", {"data-test": "DAYS_RANGE-value"}).text

            new_ticker.previous_close = previous_close
            new_ticker.open = open_price
            new_ticker.bid = bid
            new_ticker.ask = ask
            new_ticker.volume = volume
            new_ticker.avg_volume = avg_volume
            new_ticker.market_cap = market_cap
            new_ticker.earnings_date = earnings_date
            new_ticker.year_target_est = year_target_est
            new_ticker.year_range = year_range
            new_ticker.day_range = day_range

        except (ValidationError, IntegrityError, AttributeError, IndexError):
            continue

    new_ticker.save()
