from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
from datetime import datetime
# pip install lxml


def get_soup():  # when it's an RSS feed, stick to "xml" - but when it's a normal web link, use "lxml"
    html_text = requests.get(
        'https://thequietus.com/reviews.atom').text
    return BeautifulSoup(html_text, 'xml')


soup = get_soup()


def cook_soup():  # each article is in an "entry"
    return soup.find_all('entry')


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
        article_publication = 'The Quietus'
        article_RSS = 'https://thequietus.com/reviews.atom'
        article_index = idx
        article_title = article.find('title').text
        article_title_formatted = article_title.replace(
            '<i>', '').replace('</i>', '')
        article_URL = article.find('link').get('href')
        article_date = article.find('published').text
        article_date_new_format = article_date.replace('Z', '+00:00')
        '''
        standard time for this app is:
        %a, %d %b %Y %H:%M:%S %z
        2022-12-18T05:00:00+00:00
        but might need to tweak case by case
        (see flux_sub file for example of change)
        If I'm ever stuck https://www.geeksforgeeks.org/python-datetime-strptime-function/
        '''
        # article_date_formatted = datetime.strptime(
        #     article_date, "%a, %d %b %Y %H:%M:%S %z")
        # use_this_date = article_date_formatted.isoformat()
        # article_author = article.find('dc:creator').text
        article_author = article.find('author').text.strip()
        use_this_author = article_author.replace('\n', ', ')

        # fill in our lists with our loop variable values
        index_list.append(article_index)
        title_list.append(article_title_formatted)
        URL_list.append(article_URL)
        author_list.append(use_this_author)
        publication_list.append(article_publication)
        date_list.append(article_date_new_format)


deliver_soup()

# combine all my lists into a dict
quietus = [
    {'idx': idx,
     'title': title,
     'URL': URL,
     'author': author,
     'publication': publication,
     'date': date}
    for idx, title, URL, author, publication, date in zip(index_list, title_list, URL_list, author_list, publication_list, date_list)
]

# python feeds/quietus.py
