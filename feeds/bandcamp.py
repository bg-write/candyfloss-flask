from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
from datetime import datetime
# pip install lxml


# when it's an RSS feed, stick to "xml" - but when it's a normal web link, use "lxml" # todo but now this doesn't work ...
def get_soup():
    html_text = requests.get(
        'https://rss.app/feeds/m8Ku0m1gMmLpV1IC.xml').text
    return BeautifulSoup(html_text, 'xml')


soup = get_soup()


def cook_soup():  # each article is in an "item"
    return soup.find_all('item')


articles = cook_soup()

# define the empty lists we'll soon fill up with our loop
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
        article_publication = 'Bandcamp Daily'
        article_RSS = 'https://rss.app/feeds/m8Ku0m1gMmLpV1IC.xml'
        article_index = idx
        article_title = article.find('title').text
        article_URL = article.find('link').text
        article_date = article.find('pubDate').text
        '''
        standard time for this app is:
        %a, %d %b %Y %H:%M:%S %z
        but might need to tweak case by case
        (see flux_sub file for example of change)
        '''
        article_date_formatted = datetime.strptime(
            article_date, "%a, %d %b %Y %H:%M:%S %Z")
        use_this_date = article_date_formatted.isoformat()
        # todo author credit here is given to the publisher, not the writer - turning this into a strict string for now
        article_author = article.find('dc:creator').text

        # fill in our lists with our loop variable values
        index_list.append(article_index)
        title_list.append(article_title)
        URL_list.append(article_URL)
        author_list.append(article_author)
        publication_list.append(article_publication)
        date_list.append(use_this_date)


deliver_soup()

# combine all my lists into a dict
bandcamp = [
    {'idx': idx,
     'title': title,
     'URL': URL,
     'author': author,
     'publication': publication,
     'date': date}
    for idx, title, URL, author, publication, date in zip(index_list, title_list, URL_list, author_list, publication_list, date_list)
]
# python feeds/bandcamp.py
