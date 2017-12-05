
import requests
from bs4 import BeautifulSoup


def get_latest_press(code) :
    # Get HTML codes
    url = "https://www.bloomberg.com/quote/" + code
    response = requests.get(url).text

    # Get the first element of press releases
    soup = BeautifulSoup(response, "html5lib")
    # select = "#root > div > div > section.quotePageMainContent.page-modules > div.module.newsAndPressReleasesContainer__e3243a6f > div.newsAndPressReleases__d7294973 > div.pressReleasesContainer__c79992bc.selected > div > div > article:nth-of-type(1) > a > div > div.headline__eb73356e"
    select = "div.pressReleasesContainer__c79992bc.selected > div > div > article:nth-of-type(1) > a > div > div.headline__eb73356e"
    return soup.select(select)[0].text

code = "600019:CH"
press = get_latest_press(code)
print (press)