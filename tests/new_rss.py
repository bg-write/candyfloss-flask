"""

To test new RSS feeds before creating feed files.
This file name isn't included in pytest

> python tests/new_rss.py
"""
from bs4 import BeautifulSoup
import requests


def test_new_rss_external():
    '''GET request to RSS feed to make sure it works.'''
    response = requests.get(
        'https://www.theguardian.com/music/rss')
    response_soup = BeautifulSoup(response.text, 'xml')
    print(response_soup)


test_new_rss_external()

# todo for testing web scrapping when RSS isn't available
# def test_new_xml_external():
#     '''GET request from web sites without RSS feeds.'''
#     response = requests.get('')
#     response_soup = BeautifulSoup(response.text, 'lxml')
#     print(response_soup)

# test_new_xml_external()