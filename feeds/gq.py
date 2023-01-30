# todo web scraping with datetime last piece of the puzzle to fix until converting this into a class

def test_new_lxml_external():
    '''GET request from web sites without RSS feeds.'''
    response = requests.get('https://www.gq.com/about/music')
    response_soup = BeautifulSoup(response.text, 'lxml')
    return response_soup.find_all('div', class_='title-card__container')

articles = test_new_lxml_external()
# print(articles)

for idx, article in enumerate(articles):
    idx = idx
    title = article.find('h2', class_='title-card__hed').text
    author = article.find('span',
                          class_='content-type-details__author').text[3:]
    content_url = article.find('a', class_='title-card__image-link')['href']
    content_url_full = 'https://www.gq.com' + content_url

    date = article.find('span', class_='content-type-details__pub-date').text
    if date[0].isdigit():
        converted_date = (datetime.now() - timedelta(days=int(date[0])))
    else:
        converted_date = datetime.strptime(date, "%B %d, %Y")
    new_date_str = str(converted_date)[:10]
    
    date_formatted = datetime.strptime(new_date_str, "%Y-%B-%d")
    
    print(date_formatted)
    
    
    # date_formatted = datetime.strptime(new_date_str, "%Y-%m-%d %H:%M:%S%f")

    # date_formatted = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
    # date_formatted_iso = date_formatted.isoformat()

    # print(idx)
    # print(title)
    # print(author)
    # print(content_url_full)