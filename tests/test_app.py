"""

NOTES ON FUTURE PYTEST REFACTORING:
Do not use "assert" statements for validating argument values of a public API; assert is used to ensure internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred.
If an exception is desired in the latter cases, use a raise statement.
https://google.github.io/styleguide/pyguide.html

> pytest -v
"""
from app import app
import json

# Defining constants for URLs and status codes
HOME_URL = '/'
API_URL = '/api'
ENDPOINT_URL = '/api/<outlet>'
UTF_8 = 'utf-8'
STATUS_OK = 200


def test_app_index_route():
    """GET request to app's home page."""
    response = app.test_client().get(HOME_URL)
    assert response.status_code == STATUS_OK


def test_app_api_route():
    """GET request to default internal API endpoint."""
    response = app.test_client().get(API_URL)
    assert response.status_code == STATUS_OK
    res = json.loads(response.data.decode(UTF_8))
    assert type(res) is list
    assert type(res[0]) is dict
    assert type(res[1]) is dict


def test_app_api_parameters():
    """GET requests to specified internal API endpoints."""
    response = app.test_client().get(ENDPOINT_URL)
    assert response.status_code == STATUS_OK
    res = json.loads(response.data.decode(UTF_8))
    assert type(res) is list

    response_p4k = app.test_client().get('/api/Pitchfork')
    res_p4k = json.loads(response_p4k.data.decode(UTF_8))
    assert type(res_p4k) is list
    assert res_p4k[0]['publication'] == 'Pitchfork'

    response_gum = app.test_client().get('/api/Stereogum')
    res_gum = json.loads(response_gum.data.decode(UTF_8))
    assert type(res_gum) is list
    assert res_gum[0]['publication'] == 'Stereogum'