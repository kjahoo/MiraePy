
# code = ["7267:JP", "AMZN:US", "600019:CH", "005930:KR"]
#root > div > div > section.quotePageSnapshot > div.pseudoMainContent > div > section.snapshotOverview__d5769afc.up__a7674eca > section > section.company__c1979f17 > h1

import requests
from bs4 import BeautifulSoup

def bloomberg_news(code):
    url = "https://www.bloomberg.com/quote/" + code

    response = requests.get(url).text
    #soup = BeautifulSoup(html, "html.parser")

    soup = BeautifulSoup(response, "html5lib")

    stock_name = soup.select(
        "section.company__c1979f17 > h1")

    news_article = soup.select("div.headline__eb73356e")

    news_time = soup.select("div.updatedAt__3fe411c9")

    link_news = soup.select('article:nth-of-type(1) > a')

    url_news = link_news[0].get('href')

    # print(stock_name)

    return [code, stock_name[0].text, news_article[0].text, news_time[0].text, url_news]


# for i in code:
#     print(bloomberg_news(i))

# code = "600019:CH"
#
# a = bloomberg_news(code)
# print(a)

# import webbrowser
# webbrowser.open(url_news)
