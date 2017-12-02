#root > div > div > section.quotePageMainContent.page-modules > div.module.newsAndPressReleasesContainer__e3243a6f > div.newsAndPressReleases__d7294973 > div.newsContainer__8bcb508a.selected > div > div > article:nth-child(1) > a > div > div.headline__07dbac92

import requests
from bs4 import BeautifulSoup

code = "Amzn:US"
url = "https://www.bloomberg.com/quote/"+ code
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
selector = "div.newsContainer__8bcb508a.selected > div > div > article:nth-of-type(1) > a > div > div.headline__07dbac92"
tags = soup.select(selector)


print(tags[0].text)

