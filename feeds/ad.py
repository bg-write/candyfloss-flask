from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
from datetime import datetime
# pip install lxml


def get_soup():
    html_text = requests.get(
        'https://aquariumdrunkard.com/feed/').text
    return BeautifulSoup(html_text, 'xml')


soup = get_soup()


def cook_soup():  # in our rss link, each feature is in an "item"
    return soup.find_all('item')


articles = cook_soup()

# define the empty arrays we'll soon fill up with our loop
index_list = []
title_list = []
URL_list = []
author_list = []
publication_list = []
date_list = []


def deliver_soup():
    for idx, article in enumerate(articles):
        # define our variables
        # (we won't print every single one)
        article_publication = 'Aquarium Drunkard'
        article_RSS = 'https://aquariumdrunkard.com/feed/'
        article_index = idx
        article_title = article.find('title').text
        article_URL = article.find('link').text
        article_date = article.find('pubDate').text
        article_date_formatted = datetime.strptime(
            article_date, "%a, %d %b %Y %H:%M:%S %z")
        use_this_date = article_date_formatted.isoformat()
        # author credit given to pub - turning this into a strict string for now
        # article_author = article.find('dc:creator').text
        article_author = 'Aquarium Drunkard'

        # fill in our arrays with our loop variable values
        index_list.append(article_index)
        title_list.append(article_title)
        URL_list.append(article_URL)
        author_list.append(article_author)
        publication_list.append(article_publication)
        date_list.append(use_this_date)


deliver_soup()

# combine all my lists into a dict
ad = [
    {'idx': idx,
     'title': title,
     'URL': URL,
     'author': author,
     'publication': publication,
     'date': date}
    for idx, title, URL, author, publication, date in zip(index_list, title_list, URL_list, author_list, publication_list, date_list)
]
# python feeds/ad.py
