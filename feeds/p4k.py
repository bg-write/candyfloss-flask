from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
# pip install lxml


def get_soup():
    html_text = requests.get(
        'https://pitchfork.com/feed/feed-album-reviews/rss').text
    return BeautifulSoup(html_text, 'xml')


print('getting soup ...')
soup = get_soup()
print("soup got!")


def cook_soup():  # each p4k review is in an "item"
    return soup.find_all('item')


print('cooking soup ...')
reviews = cook_soup()
print('soup cooked!')

# define empty arrays that we'll soon fill up with our loop
review_title_arr = []
review_URL_arr = []
review_author_arr = []
review_publication_arr = []


def deliver_soup():
    for review in reviews:
        # define our variables (we won't print every one)
        review_publication = 'Pitchfork'
        review_RSS = 'https://pitchfork.com/feed/feed-album-reviews/rss'
        review_title = review.find('title').text
        review_URL = review.find('link').text
        review_ID = review.find('guid').text
        review_date = review.find('pubDate').text
        review_description = review.find('description').text
        review_category = review.find('category').text
        media_keywords = review.find('media:keywords').text if review.find(
            'media:keywords') else ''
        review_author = review.find('dc:creator').text
        review_publisher = review.find('dc:publisher').text

        # fill in our arrays with our loop variable values
        review_title_arr.append(review_title)
        review_URL_arr.append(review_URL)
        review_author_arr.append(review_author)
        review_publication_arr.append(review_publication)


print('delivering soup ...')
deliver_soup()
print('soup delivered!')

# print(review_title_arr)
# print(review_URL_arr)
# print(review_author_arr)
# print(review_publication_arr)

# python feeds/p4k.py
