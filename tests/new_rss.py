"""

To test new RSS feeds before creating feed files.
This file isn't included in pytest.

> python tests/new_rss.py
"""
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

current_date = datetime.now().strftime("%B %d, %Y")
# print(current_date)


def test_new_rss_external():
    '''GET request to RSS feed to make sure it works.'''
    response = requests.get('https://van-magazine.com/feed/')
    response_soup = BeautifulSoup(response.text, 'xml')
    print(response_soup)


test_new_rss_external()


def test_new_lxml_external():
    '''GET request to sites without RSS feeds (scraping).'''
    response = requests.get('https://www.gq.com/about/music')
    response_soup = BeautifulSoup(response.text, 'lxml')
    return response_soup.find_all('div', class_='title-card__container')


articles = test_new_lxml_external()
# print(articles)
