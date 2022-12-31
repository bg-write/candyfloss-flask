"""

> pytest -v
"""
from app import link_dicts_sorted_and_reduced

def test_app():
    '''asserting each app module (need to flesh out)'''
    assert isinstance(link_dicts_sorted_and_reduced, list)

# Do not use assert statements for validating argument values of a public API
# Assert is used to ensure internal correctness
# not to enforce correct usage
# Nor to indicate that some unexpected event occurred.
# If an exception is desired in the latter cases
# Use a raise statement
# https://google.github.io/styleguide/pyguide.html
