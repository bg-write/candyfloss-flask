"""

NOTES ON PYTEST REFACTORING:
Do not use "assert" statements for validating argument values of a public API; assert is used to ensure internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred.
If an exception is desired in the latter cases, use a raise statement.
https://google.github.io/styleguide/pyguide.html

> pytest -v
"""
from app import app
from feeds.p4k_class import pitchfork
from feeds.gum import gum
import requests
import json

# Defining constants for URLs and status codes
UTF_8 = 'utf-8'
STATUS_OK = 200


def test_feed_p4k_external():
    '''GET request to Pitchfork's RSS feed'''
    response = requests.get(pitchfork.feed_url)
    assert response.status_code == STATUS_OK


def test_feed_p4k_internal():
    '''GET request to our Pitchfork API endpoint'''
    response = app.test_client().get('/api/Pitchfork')
    assert response.status_code == 200
    res_p4k = json.loads(response.data.decode(UTF_8))
    assert type(res_p4k) is list
    assert type(res_p4k[0]) is dict
    assert type(res_p4k[1]) is dict
    assert res_p4k[0]['publication'] == 'Pitchfork'


def test_feed_stereogum_external():
    '''GET request to Stereogum's RSS feed'''
    # todo need to refactor gum.py to new class structure
    response = requests.get('https://www.stereogum.com/category/music/feed/')
    assert response.status_code == STATUS_OK


def test_feed_stereogum_internal():
    '''GET request to our Stereogum API endpoint'''
    response = app.test_client().get('/api/Stereogum')
    assert response.status_code == STATUS_OK
    res_gum = json.loads(response.data.decode(UTF_8))
    assert type(res_gum) is list
    assert type(res_gum[0]) is dict
    assert type(res_gum[1]) is dict
    assert res_gum[0]['publication'] == 'Stereogum'