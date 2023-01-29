"""

NOTES ON PYTEST REFACTORING:
Do not use "assert" statements for validating argument values of a public API; assert is used to ensure internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred.
If an exception is desired in the latter cases, use a raise statement.
https://google.github.io/styleguide/pyguide.html

> pytest -v
"""
from app import app
from feeds.p4k_class import pitchfork
import requests
import json


def test_feed_p4k_external():
    '''GET request to Pitchfork's RSS feed'''
    response = requests.get(pitchfork.feed_url)
    assert response.status_code == 200


def test_feed_p4k_internal():
    '''GET request to our Pitchfork API endpoint'''
    response = app.test_client().get('/api/Pitchfork')
    assert response.status_code == 200
    res_p4k = json.loads(response.data.decode('utf-8'))
    assert type(res_p4k) is list
    assert type(res_p4k[0]) is dict
    assert type(res_p4k[1]) is dict
    assert res_p4k[0]['publication'] == 'Pitchfork'
