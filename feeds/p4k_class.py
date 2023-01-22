"""

Call and clean our RSS feed with only the information we need.
Imports include py's datetime, Beautiful Soup, and requests.
Can also import lxml when RSS url is not available.
"""
from datetime import datetime
from bs4 import BeautifulSoup
import requests


class Outlet(object):
    """Online feeds with URLs to scrap and display its content to users.

  Attributes:
    feed_url: i.e. https://pitchfork.com/feed/feed-album-reviews/rss
    publication: i.e. 'Pitchfork'
    idx: i.e. 7
    title: i.e. 'Jumping/Dancing/Fighting EP'
    author: i.e. 'Brady Gerber'
    url: i.e. 'https://pitchfork.com/reviews/albums/hammok-jumping-dancing-fighting-ep'
    date: i.e. '2022-12-30T05:00:00+00:00'
  """

    def __init__(self,
                 feed_url='FEED_URL',
                 publication='PUBLICATION',
                 idx=0,
                 title='TITLE',
                 author='AUTHOR',
                 content_url='CONTENT_URL',
                 date='DATE'):
        """Inits Outlet with our constructor and placeholders."""
        self.feed_url = feed_url
        self.publication = publication
        self.idx = idx
        self.title = title
        self.author = author
        self.content_url = content_url
        self.date = date

    def __str__(self):
        """Returns the string representation of the object."""
        return (
            f'{self.idx}: {self.title} ({self.author} / {self.publication}) ({self.content_url}) ({self.date}) ({self.feed_url})'
        )

    def console(self):
        """Prints our string representation to the console and each attribute."""
        print(self)
        print(self.feed_url)
        print(self.publication)
        print(self.idx)
        print(self.title)
        print(self.author)
        print(self.content_url)
        print(self.date)

    def get_soup(self):
        """Make our initial GET request to our RSS feed."""
        html_text = requests.get(self.feed_url, timeout=10).text
        return BeautifulSoup(html_text, 'xml')


pitchfork = Outlet('https://pitchfork.com/feed/feed-album-reviews/rss',
                   'Pitchfork')
soup = pitchfork.get_soup()


def cook_soup():
    """In this specific RSS link, each review is in an <item/> tag."""
    return soup.find_all('item')


articles = cook_soup()

# Define the empty lists we'll soon fill up with deliver_soup().
idx_list = []
title_list = []
author_list = []
content_url_list = []
date_list = []


def deliver_soup():
    """Append only the info we need from our articles soup using a For loop."""
    for idx, article in enumerate(articles):
        idx = idx
        title = article.find('title').text
        author = article.find('dc:creator').text
        content_url = article.find('link').text
        date = article.find('pubDate').text
        date_formatted = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
        date_formatted_iso = date_formatted.isoformat()

        idx_list.append(idx)
        title_list.append(title)
        author_list.append(author)
        content_url_list.append(content_url)
        date_list.append(date_formatted_iso)


deliver_soup()

# zip all my lists, now full of the data we need, into a list of dictionaries for this specific outlet
p4k = [
    {
        'idx': idx,
        'title': title,
        'content_url': content_url,
        'author': author,
        'publication': pitchfork.publication,  # same value for each dict
        'date': date
    } for idx, title, content_url, author, date in zip(
        idx_list, title_list, content_url_list, author_list, date_list)
]
print(p4k)

# python feeds/p4k_class.py
