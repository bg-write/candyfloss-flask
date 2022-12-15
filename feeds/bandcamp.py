from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
from datetime import datetime
# pip install lxml


def get_soup():  # when it's an RSS feed, stick to "xml" - but when it's a normal web link, use "lxml"
    html_text = requests.get(
        'https://rss.app/feeds/m8Ku0m1gMmLpV1IC.xml').text
    return BeautifulSoup(html_text, 'xml')


print('getting soup ...')
soup = get_soup()
print("soup got!")
# print(soup)


def cook_soup():  # each article is in an "item"
    return soup.find_all('item')


print('cooking soup ...')
articles = cook_soup()
print('soup cooked!')
# print(articles)

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


print('delivering soup ...')
deliver_soup()
print('soup delivered!')

# print(index_list)
# print(title_list)
# print(URL_list)
# print(author_list)
# print(publication_list)
# print(date_list)

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
# print(bandcamp)

# python feeds/bandcamp.py
