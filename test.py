import requests
import pprint
from bs4 import BeautifulSoup as bs


url = "https://finance.yahoo.com"
content = requests.get(url).content
pprint.pprint(content)
soup = bs(content, "html.parser")
cadru_news = soup.find_all("div", {"class": "Cf"})
cadru_mare = soup.find_all("div", "Py(14px) Pos(r)")
# print(len(cadru_news))
# print(len(cadru_mare))
for elem in cadru_news[3:]:
    try:
        titlu = elem.find("a").text
        # print(titlu)

        p = elem.find("p").text
        # print(p)

        url = elem.find('a').get('href')
        # print(url)

        img =elem.find("img").get("src")
        # print(img)

    except AttributeError:
        continue


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

