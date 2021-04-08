import requests
import pprint
from bs4 import BeautifulSoup as bs

requests.packages.urllib3.disable_warnings()

# url = "https://finance.yahoo.com"
url2 = "https://finance.yahoo.com/quote/ASRT?p=ASRT"

# content = requests.get(url).content


# soup = bs(content, "html.parser")
# cadru_news = soup.find_all("div", {"class": "Cf"})
# cadru_mare = soup.find_all("div", "Py(14px) Pos(r)")


soup2 = bs(requests.get(url2, verify=False).content, "html.parser")
cadru_mare = soup2.find_all("div", {"id": "quote-summary"})
# titlu = soup2.find_all('div', {"class": "D(ib)"})

for i in cadru_mare:
    try:

        pc2 = i.find("span", {"data-reactid": "44"}).text
        # print(pc2)
        previous_close = i.find("td", {"data-test": "PREV_CLOSE-value"}).text
        open_price = i.find("td", {"data-test": "OPEN-value"}).text
        bid = i.find("td", {"data-reactid": "53"}).text
        ask = i.find("td", {"data-test": "ASK-value"}).text
        volume = i.find("td", {"data-test": "TD_VOLUME-value"}).text
        avg_volume = i.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text
        market_cap = i.find("td", {"data-test": "MARKET_CAP-value"}).text
        earnings_date = i.find("td", {"data-test": "EARNINGS_DATE-value"}).text
        year_target_est = i.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text
        year_range = i.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text
        day_range = i.find("td", {"data-test": "DAYS_RANGE-value"}).text
        cadru_current_price = soup2.find_all("div", {"class": "D(ib) Mend(20px)"})

    except AttributeError:
        continue

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
