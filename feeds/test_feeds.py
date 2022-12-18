from p4k import soup, reviews, index_list, title_list, URL_list, author_list, publication_list, date_list, p4k
from gum import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, gum


def test_p4k():
    assert soup
    assert reviews
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert p4k


def test_gum():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert gum


'''NOTES ON PYTEST
Files must have format test_XXX.py or XXX_test.py
Test methods should start wth keyword "test"

> pytest (more details)
> pytest -q (less details)
'''

# python feeds/test_feeds.py
