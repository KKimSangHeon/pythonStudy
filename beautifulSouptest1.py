import requests, urllib
from bs4 import BeautifulSoup as bs
def download_image(img_src, filename):
    res = urllib.request.urlretrieve(img_src, filename)
    return res


def crawl_text():
    res = requests.get('https://schema.org/Movie')
    if res.status_code == 200:
        soup = bs(res.text, 'lxml')
        images = soup.select('#mainContent > table > tbody > tr > td')

        for image in images:
            print(image.get_text())



crawl_text()

