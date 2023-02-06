"""

To test new RSS feeds before creating feed files.
This file isn't included in pytest.

> python tests/new_rss.py
"""
from bs4 import BeautifulSoup
from datetime import datetime
import requests

current_date = datetime.now().strftime("%B %d, %Y")
# print(current_date)


def test_new_rss_external():
    '''GET request to RSS feed to make sure it works.'''
    response = requests.get('https://www.opemag.com/rss.xml')
    response_soup = BeautifulSoup(response.text, 'xml')
    print(response_soup)


# test_new_rss_external()


def test_new_lxml_external():
    '''GET request to sites without RSS feeds (scraping).'''
    response = requests.get('https://www.wsj.com/news/types/music-review/')
    print(response.status_code)
    response_soup = BeautifulSoup(response.text, 'lxml')
    # print(response_soup)
    articles = response_soup.find_all('a', class_='item')
    # print(articles)

# test_new_lxml_external()
