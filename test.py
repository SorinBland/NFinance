import requests
import pprint
from bs4 import BeautifulSoup as bs
import re

requests.packages.urllib3.disable_warnings()

# url = "https://finance.yahoo.com"
# url2 = "https://finance.yahoo.com/quote/asrt?p=asrt"

# content = requests.get(url).content
session = requests.Session()
session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
url = "https://www.wsj.com/news/business?mod=hp_lista_strap"
soup = bs(session.get(url, verify=False).content, "html.parser")
cadru_news1 = soup.find_all("article",
                            {
                                "class": "WSJTheme--story--XB4V2mLz WSJTheme--story-padding--1gRL3tuf "
                                         "WSJTheme--border-bottom--s4hYCt0s"})
cadru_news2 = soup.find_all("article", {
    "class": "WSJTheme--story--XB4V2mLz WSJTheme--story-padding--1gRL3tuf WSJTheme--media-margin-bottom--1bIRFuDR "
             "WSJTheme--border-bottom--s4hYCt0s"})

for article in cadru_news1[1:]:
    try:
        title = article.find("h3").text
        paragraph = article.find("p").text
        url = article.find("a").get("href")
        img = article.find("img").get("src")
        # print(paragraph)
        if paragraph.rsplit(".")[-1].isnumeric():
            print("".join(paragraph.rsplit(".")[:-1]))
        # print(paragraph.rsplit("."))

    except AttributeError:
        continue

for article2 in cadru_news2:
    try:
        title2 = article2.find("h3").text
        paragraph2 = article2.find("p").text
        url2 = article2.find("a").get("href")
        img2 = article2.find("img").get("src")
        # print(title2)
        # print(paragraph2)
    except AttributeError:
        continue

# soup = bs(content, "html.parser")
# cadru_news = soup.find_all("div", {"class": "Cf"})
# cadru_mare = soup.find_all("div", "Py(14px) Pos(r)")


# soup2 = bs(requests.get(url2, verify=False).content, "html.parser")
# cadru_mare = soup2.find_all("div", {"id": "quote-summary"})
######################################
# cadru_company_profile = soup2.find_all("div", {"data-reactid": "58"})
# cadru_company_profile2 = soup2.p['class']
# print(cadru_company_profile2)

# for cp in cadru_company_profile:
#     try:
# company_profile = cp.find("p", {"class": "businessSummary Mt(10px) Ov(h) Tov(e)"})
# company_profile = cp.find_all("p")
# print(cp.prettify())
# print(company_profile.text)

# except AttributeError:
#     continue

# for elem in titlu:
#     try:
#         title = elem.find("h1").text
#
#         tick_from_title = re.findall(r'\(.*?\)', title)
#         for tick in tick_from_title:
#             print(str(tick).strip("()"))
#
#     except AttributeError:
#         continue

# for i in cadru_mare:
#     try:

# pc2 = i.find("span", {"data-reactid": "44"}).text
# print(pc2)
# previous_close = i.find("td", {"data-test": "PREV_CLOSE-value"}).text
# print(previous_close)
# open_price = i.find("td", {"data-test": "OPEN-value"}).text
# bid = i.find("td", {"data-reactid": "53"}).text
# ask = i.find("td", {"data-test": "ASK-value"}).text
# volume = i.find("td", {"data-test": "TD_VOLUME-value"}).text
# avg_volume = i.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text
# market_cap = i.find("td", {"data-test": "MARKET_CAP-value"}).text
# earnings_date = i.find("td", {"data-test": "EARNINGS_DATE-value"}).text
# year_target_est = i.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text
# year_range = i.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text
# day_range = i.find("td", {"data-test": "DAYS_RANGE-value"}).text
# cadru_current_price = soup2.find_all("div", {"class": "D(ib) Mend(20px)"})

# except AttributeError:
#     continue


# for i in titlu:
#     try:
#         t = i.find("h1").text
#         print(t)
#
#     except AttributeError:
#         continue


# for elem in cadru_news[3:]:
#     try:
#         titlu = elem.find("a").text
#         # print(titlu)
#
#         p = elem.find("p").text
#         # print(p)
#
#         url = elem.find('a').get('href')
#         # print(url)
#
#         img = elem.find("img").get("src")
#         # print(img)
#
#     except AttributeError:
#         continue

# try:
#     for article in cadru_news:
#         articol = article.find_all("p")
#         remove_list = ["AFP", "Yahoo Finance", "Yahoo Money", "Reuters", "Yahoo Finance Video"]
#
#             # print(article.find_all("a"), end="\n")
#         pprint.pprint(articol[0].text)
# except IndexError:
#     pass
# for article in cadru_mare:
# try:
# div_cf = article.find_all("div", {"class": "Cf"})
# lista = article.find_all("li", {"class": "js-stream-content"})

# for i in div_cf:
#     articol = i.find_all("h3")
#     for e in articol:
#         t = e.find_all("a")
#         print(t)

# for titlu_mic in articol:
#     t2 = titlu_mic.find_all("h3")
# for elem in t2:
# print(elem.tex)

# except IndexError:
#     continue
