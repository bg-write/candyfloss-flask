from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
from datetime import datetime
# pip install lxml


def get_soup():
    html_text = requests.get(
        'https://pitchfork.com/feed/feed-album-reviews/rss').text
    return BeautifulSoup(html_text, 'xml')


print('getting soup ...')
soup = get_soup()
print("soup got!")


def cook_soup():  # in our rss link, each p4k review is in an "item"
    return soup.find_all('item')


print('cooking soup ...')
reviews = cook_soup()
print('soup cooked!')

# define the empty lists we'll soon fill up with our loop
index_list = []
title_list = []
URL_list = []
author_list = []
publication_list = []
date_list = []


def deliver_soup():
    for idx, review in enumerate(reviews):
        # define our variables (we won't print every single one)
        review_publication = 'Pitchfork'
        review_RSS = 'https://pitchfork.com/feed/feed-album-reviews/rss'
        review_index = idx
        review_title = review.find('title').text
        review_URL = review.find('link').text
        review_ID = review.find('guid').text
        review_date = review.find('pubDate').text
        review_date_formatted = datetime.strptime(
            review_date, "%a, %d %b %Y %H:%M:%S %z")
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


print('delivering soup ...')
deliver_soup()
print('soup delivered!')

# print(review_index_list)
# print(review_title_list)
# print(review_URL_list)
# print(review_author_list)
# print(review_publication_list)
# print(review_date_list)

# combine all my lists into a p4k dict
p4k = [
    {'idx': idx,
     'title': title,
     'URL': URL,
     'author': author,
     'publication': publication,
     'date': date}
    for idx, title, URL, author, publication, date in zip(index_list, title_list, URL_list, author_list, publication_list, date_list)
]
'''
[
    {'idx': 0, 'title': 'Watertown', 'URL': 'https://pitchfork.com/reviews/albums/frank-sinatra-watertown', 'author': 'Sam Sodomsky', 'publication': 'Pitchfork', 'date': '2022-12-11T05:00:00+00:00'},
    {'idx': 1, 'title': 'Divine Symmetry', 'URL': 'https://pitchfork.com/reviews/albums/david-bowie-divine-symmetry', 'author': 'Jane Bua', 'publication': 'Pitchfork', 'date': '2022-12-10T05:00:00+00:00'},
    {'idx': 2, 'title': 'SOS', 'URL': 'https://pitchfork.com/reviews/albums/sza-sos', 'author': 'Julianne Escobedo Shepherd', 'publication': 'Pitchfork', 'date': '2022-12-09T05:02:00+00:00'}
]
'''

# print(p4k)
# print(p4k[0]['idx'])
# print(p4k[0]['title'])
# print(p4k[0]['URL'])
# print(p4k[0]['author'])
# print(p4k[0]['publication'])
# print(p4k[0]['date'])

# python feeds/p4k.py
