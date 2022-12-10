from bs4 import BeautifulSoup  # pip install bs4
import requests  # pip install requests
# pip install lxml


def get_soup(): 
    html_text = requests.get(
        'https://www.stereogum.com/category/reviews/album-of-the-week/feed/').text
    return BeautifulSoup(html_text, 'xml')


print('getting soup ...')
soup = get_soup()
print("soup got!")


def cook_soup():  # in our rss link, each stereogum feature is in an "item"
    return soup.find_all('item')


print('cooking soup ...')
articles = cook_soup()
print('soup cooked!')

# define the empty arrays we'll soon fill up with our loop
article_title_arr = []
article_URL_arr = []
article_author_arr = []
article_publication_arr = []


def deliver_soup():
    for article in articles:
        # define our variables (we won't print every single one)
        article_publication = 'Stereogum'
        article_RSS = 'https://www.stereogum.com/category/reviews/album-of-the-week/feed/'
        
        article_title = article.find('title').text
        article_URL = article.find('link').text
        article_date = article.find('pubDate').text
        article_author = article.find('dc:creator').text

        # fill in our arrays with our loop variable values
        article_title_arr.append(article_title)
        article_URL_arr.append(article_URL)
        article_author_arr.append(article_author)
        article_publication_arr.append(article_publication)


print('delivering soup ...')
deliver_soup()
print('soup delivered!')

# print(article_title_arr)
# print(article_URL_arr)
# print(article_author_arr)
# print(article_publication_arr)

# python feeds/gum.py