
# code = ["7267:JP", "AMZN:US", "60019:CH", "005930:KR"]


import requests
from bs4 import BeautifulSoup

def bloomberg_news(code):
    url = "https://www.bloomberg.com/quote/" + code
    response = requests.get(url).text
    #soup = BeautifulSoup(html, "html.parser")

    soup = BeautifulSoup(response, "html5lib")
    if code[-2:] == "CH":

        news = "div.pressReleasesContainer__c79992bc.selected > div > div > article:nth-of-type(1) > a > div > div.headline__eb73356e"
        news_article = soup.select(news)

        news_time = soup.select("div.pressReleasesContainer__c79992bc.selected > div > div > article:nth-of-type(1) > a > div > div.updatedAt__3fe411c9")
        link_news = soup.select('div.pressReleasesContainer__c79992bc.selected > div > div > article:nth-of-type(1) > a')

    else:
        news = "div.newsContainer__8bcb508a.selected > div > div > article:nth-of-type(1) > a > div > div.headline__07dbac92"
        news_article = soup.select(news)

        news_time = soup.select("div.newsContainer__8bcb508a.selected > div > div > article:nth-of-type(1) > a > div > div.publishedAt__4009bb4f")

        link_news = soup.select('div.newsContainer__8bcb508a.selected > div > div > article:nth-of-type(1) > a')

    for title in link_news:
        url_news = title.get('href')

    return [news_article[0].text, news_time[0].text, url_news]


# for i in code:
#     print(bloomberg_news(i))

code = "600019:CH"

a = bloomberg_news(code)
print(a)

# import webbrowser
# webbrowser.open(url_news)
