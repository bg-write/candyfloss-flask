"""

Call and clean the RSS feed with only the information we need.
Imports include Py's datetime, Beautiful Soup, and requests.
Can also import lxml when RSS url is not available.
"""
from datetime import datetime
from bs4 import BeautifulSoup
import requests


class Outlet(object):
    """Online feeds with URLs to scrap and display to users.

  Attributes:
    feed_url: i.e. https://pitchfork.com/feed/feed-album-reviews/rss
    title: i.e. 'Jumping/Dancing/Fighting EP'
    author: i.e. 'Brady Gerber'
    publication: i.e. 'Pitchfork'
    url: i.e. 'https://pitchfork.com/reviews/albums/hammok-jumping-dancing-fighting-ep'
    date: i.e. '2022-12-30T05:00:00+00:00'
  """

    def __init__(self,
                 feed_url='FEED_URL',
                 title='TITLE',
                 author='AUTHOR',
                 publication='PUBLICATION',
                 content_url='CONTENT_URL',
                 date='DATE'):
        """Inits Outlet with our constructor and placeholders."""
        self.feed_url = feed_url
        self.title = title
        self.author = author
        self.publication = publication
        self.content_url = content_url
        self.date = date

    def __str__(self):
        """Returns the string representation of the object."""
        return (
            f'{self.title} ({self.author} / {self.publication}) ({self.content_url}) ({self.date}) ({self.feed_url})'
        )

    def console(self):
        """Prints our string representation to the console and each attribute."""
        print(self)
        print(self.feed_url)
        print(self.title)
        print(self.author)
        print(self.publication)
        print(self.content_url)
        print(self.date)

    def get_soup(self):
        """Make our initial GET request to our RSS feed."""
        html_text = requests.get(self.feed_url, timeout=10).text
        return BeautifulSoup(html_text, 'xml')


# creating a new "Outlet" object called "pitchfork"
pitchfork = Outlet('https://pitchfork.com/feed/feed-album-reviews/rss')
# pitchfork.console()

soup = pitchfork.get_soup()
print(soup)

# python feeds/p4k_class.py
