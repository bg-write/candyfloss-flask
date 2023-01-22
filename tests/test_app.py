"""

NOTES ON FUTURE PYTEST REFACTORING:
Do not use "assert" statements for validating argument values of a public API; assert is used to ensure internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred.
If an exception is desired in the latter cases, use a raise statement.
https://google.github.io/styleguide/pyguide.html
"""
from app import link_dicts_sorted_and_reduced


def test_app():
    '''Asserting each app module.'''
    assert isinstance(link_dicts_sorted_and_reduced, list)
