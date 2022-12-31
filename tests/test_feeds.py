"""

> pytest -v
"""
from feeds.p4k import p4k
# from feeds.p4k import soup, reviews, index_list, title_list, URL_list, author_list, publication_list, date_list, p4k
# from feeds.gum import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, gum
# from feeds.ad import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, ad
# from feeds.ringer import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, ringer
# from feeds.flux_sub import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, flux_sub
# from feeds.MJI import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, MJI
# from feeds.penny import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, penny
# from feeds.chi_reader import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, chi_reader
# from feeds.uproxx import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, uproxx
# from feeds.abundant_living import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, abundant_living
# from feeds.billboard_chart_beat import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, billboard_chart_beat
# from feeds.no_bells import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, no_bells
# from feeds.quietus import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, quietus
# from feeds.loud_quiet import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, loud_quiet
# from feeds.no_depression import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, no_depression
# from feeds.sterlewine import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, so_it_goes
# from feeds.reply_alt import soup, articles, index_list, title_list, URL_list, author_list, publication_list, date_list, reply_alt


def test_p4k():
    '''Pitchfork'''
    assert isinstance(p4k, list)
    # assert all(isinstance(item, int) for item in [key['idx'] for key in p4k])
    # assert all(isinstance(item, str) for item in [key['title'] for key in p4k])
    # assert all(isinstance(item, str) for item in [key['URL'] for key in p4k])
    # assert all(
    #     isinstance(item, str) for item in [key['author'] for key in p4k])
    # assert all(
    #     isinstance(item, str) for item in [key['publication'] for key in p4k])
    # assert all(isinstance(item, str) for item in [key['date'] for key in p4k])


# def test_gum():
#     '''Stereogum'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert gum == gum

# def test_ad():
#     '''Aquarium Drunkard'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert ad == ad

# def test_ringer():
#     '''The Ringer'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert ringer == ringer

# def test_flux():
#     '''Fluxblog'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert flux_sub == flux_sub

# def test_MJI():
#     '''Music Journalism Insider'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert MJI == MJI

# def test_penny():
#     '''Penny Fractions'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert penny == penny

# def test_chi_reader():
#     '''Chicago Reader'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert chi_reader == chi_reader

# def test_uproxx():
#     '''Uproxx'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert uproxx == uproxx

# def test_abundant():
#     '''Abundant Living'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert abundant_living == abundant_living

# def test_billboard():
#     '''Billboard'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert billboard_chart_beat == billboard_chart_beat

# def test_no_bells():
#     '''No Bells'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert no_bells == no_bells

# def test_quietus():
#     '''The Quietus'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert quietus == quietus

# def test_loud_quiet():
#     '''Loud & Quiet'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert loud_quiet == loud_quiet

# def test_no_depression():
#     '''No Depression'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert no_depression == no_depression

# def test_sterlewine():
#     '''So It Goes'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert so_it_goes == so_it_goes

# def test_reply_alt():
#     '''Reply Alt'''
#     assert soup
#     assert articles
#     assert index_list
#     assert title_list
#     assert URL_list
#     assert author_list
#     assert publication_list
#     assert date_list
#     assert reply_alt == reply_alt

# Do not use assert statements for validating argument values of a public API
# Assert is used to ensure internal correctness
# not to enforce correct usage
# Nor to indicate that some unexpected event occurred.
# If an exception is desired in the latter cases
# Use a raise statement
# https://google.github.io/styleguide/pyguide.html
