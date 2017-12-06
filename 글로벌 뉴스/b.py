import requests
from bs4 import BeautifulSoup

code = "AMZN:US"
url = "https://www.bloomberg.com/quote/" + code
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

# soup = BeautifulSoup(response, "html5lib")

stock_name = soup.select(
    "#root > div > div > section.quotePageSnapshot > div.pseudoMainContent > div > section.snapshotOverview__d5769afc.up__a7674eca > section > section.company__c1979f17 > h1")

# if code[-2:] == "CH":

news_article = soup.select("div.headline__eb73356e")

news_time = soup.select("div.updatedAt__3fe411c9")

link_news = soup.select('article:nth-of-type(1) > a')

# print(news_article)
# print(news_time)
# print(link_news)

'href' in link_news

# else:
#     print("a")
#     news_article = soup.select("#root > div > div > section.quotePageMainContent.page-modules > div.module.newsAndPressReleasesContainer__e3243a6f > div.newsAndPressReleases__d7294973 > div.pressReleasesContainer__c79992bc.selected > div > div > article:nth-of-type(1) > a > div > div.headline__eb73356e")
#
#     news_time = soup.select("#root > div > div > section.quotePageMainContent.page-modules > div.module.newsAndPressReleasesContainer__e3243a6f > div.newsAndPressReleases__d7294973 > div.newsContainer__8bcb508a.selected > div > div > article:nth-of-type(1) > a > div > div.publishedAt__4009bb4f")
#
#     link_news = soup.select('#root > div > div > section.quotePageMainContent.page-modules > div.module.newsAndPressReleasesContainer__e3243a6f > div.newsAndPressReleases__d7294973 > div.newsContainer__8bcb508a.selected > div > div > article:nth-of-type(1) > a')

url_news = link_news[0].get('href')
print([code, stock_name[0].text, news_article[0].text, news_time[0].text, url_news])