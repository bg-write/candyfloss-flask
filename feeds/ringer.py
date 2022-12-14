from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
# from datetime import datetime
# pip install lxml


def get_soup():
    html_text = requests.get(
        'https://www.theringer.com/rss/music/index.xml').text
    return BeautifulSoup(html_text, 'xml')


print('getting soup ...')
soup = get_soup()
print("soup got!")
# print(soup)


def cook_soup():  # each article is in an "entry"
    return soup.find_all('entry')


print('cooking soup ...')
articles = cook_soup()
print('soup cooked!')
# print(articles)

# # define the empty lists we'll soon fill up with our loop
index_list = []
title_list = []
URL_list = []
author_list = []
publication_list = []
date_list = []


def deliver_soup():
    for idx, article in enumerate(articles):
        # define our variables (we won't print every single one)
        article_publication = 'The Ringer'
        article_RSS = 'https://www.theringer.com/rss/music/index.xml'
        article_index = idx
        article_title = article.find('title').text
        article_URL = article.find('id').text
        article_date = article.find('published').text
        # article_date_formatted = datetime.strptime(
        #     article_date, "%a, %d %b %Y %H:%M:%S %z")
        # use_this_date = article_date_formatted.isoformat()
        # for when I'm dealing with multiple names in one author tag ...
        # article_author = article.find('author').text
        article_author = article.find('author').text.strip()
        use_this_author = article_author.replace('\n', ', ')
        print(use_this_author)

        # fill in our lists with our loop variable values
        index_list.append(article_index)
        title_list.append(article_title)
        URL_list.append(article_URL)
        author_list.append(use_this_author)
        publication_list.append(article_publication)
        date_list.append(article_date)


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
ringer = [
    {'idx': idx,
     'title': title,
     'URL': URL,
     'author': author,
     'publication': publication,
     'date': date}
    for idx, title, URL, author, publication, date in zip(index_list, title_list, URL_list, author_list, publication_list, date_list)
]
# print(ringer)

# python feeds/ringer.py
