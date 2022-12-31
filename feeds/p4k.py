'''
Imports Python datetime module
Imports Beautiful Soup (> pip install bs4)
Imports requests (> pip install requests)
Also can take advantage of lxml (> pip install lxml)
'''
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def get_soup():
    '''GET request'''
    html_text = requests.get(
        'https://pitchfork.com/feed/feed-album-reviews/rss').text
    return BeautifulSoup(html_text, 'xml')


soup = get_soup()


def cook_soup():
    '''In this RSS link, each review is in an "item"'''
    return soup.find_all('item')


reviews = cook_soup()

# define the empty lists we'll soon fill up with our loop
index_list = []
title_list = []
URL_list = []
author_list = []
publication_list = []
date_list = []


def deliver_soup():
    '''append needed info from for loop to our lists'''
    for idx, review in enumerate(reviews):
        # define our variables
        # (we won't print every single one)
        review_publication = 'Pitchfork'
        review_RSS = 'https://pitchfork.com/feed/feed-album-reviews/rss'
        review_index = idx
        review_title = review.find('title').text
        review_URL = review.find('link').text
        review_ID = review.find('guid').text
        review_date = review.find('pubDate').text
        review_date_formatted = datetime.strptime(review_date,
                                                  "%a, %d %b %Y %H:%M:%S %z")
        use_this_date = review_date_formatted.isoformat()
        review_description = review.find('description').text
        review_category = review.find('category').text
        media_keywords = review.find('media:keywords').text if review.find(
            'media:keywords') else ''
        review_author = review.find('dc:creator').text
        review_publisher = review.find('dc:publisher').text

        # fill in our lists with our loop variable values
        index_list.append(review_index)
        title_list.append(review_title)
        URL_list.append(review_URL)
        author_list.append(review_author)
        publication_list.append(review_publication)
        date_list.append(use_this_date)


deliver_soup()

# combine all my lists into a p4k dict
p4k = [{
    'idx': idx,
    'title': title,
    'URL': URL,
    'author': author,
    'publication': publication,
    'date': date
} for idx, title, URL, author, publication, date in zip(
    index_list, title_list, URL_list, author_list, publication_list, date_list)
       ]
# python feeds/p4k.py
