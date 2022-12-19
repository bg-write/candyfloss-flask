from p4k import soup, reviews, index_list, title_list, URL_list, author_list, publication_list, date_list, p4k
from gum import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, gum
from ad import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, ad
from ringer import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, ringer
from flux_sub import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, flux_sub
from MJI import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, MJI
from penny import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, penny
from chi_reader import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, chi_reader
from uproxx import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, uproxx
from abundant_living import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, abundant_living
from billboard_chart_beat import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, billboard_chart_beat
from bandcamp import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, bandcamp
from no_bells import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, no_bells
from quietus import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, quietus
from loud_quiet import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, loud_quiet
from no_depression import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, no_depression


def test_p4k():
    assert soup
    assert reviews
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert p4k == p4k


def test_gum():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert gum == gum


def test_ad():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert ad == ad


def test_ringer():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert ringer == ringer


def test_flux():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert flux_sub == flux_sub


def test_MJI():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert MJI == MJI


def test_penny():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert penny == penny


def test_chi_reader():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert chi_reader == chi_reader


def test_uproxx():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert uproxx == uproxx


def test_abundant():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert abundant_living == abundant_living


def test_billboard():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert billboard_chart_beat == billboard_chart_beat


def test_bandcamp():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert bandcamp == bandcamp


def test_no_bells():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert no_bells == no_bells


def test_quietus():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert quietus == quietus


def test_loud_quiet():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert loud_quiet == loud_quiet


def test_no_depression():
    assert soup
    assert articles
    assert index_list
    assert title_list
    assert URL_list
    assert author_list
    assert publication_list
    assert date_list
    assert no_depression == no_depression


'''NOTES ON PYTEST
Files must have format test_XXX.py or XXX_test.py
Test methods should start wth keyword "test"

> pytest (more details)
> pytest -q (less details)
'''
