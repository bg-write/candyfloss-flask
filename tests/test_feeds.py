"""

NOTES ON FUTURE PYTEST REFACTORING:
Do not use "assert" statements for validating argument values of a public API; assert is used to ensure internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred.
If an exception is desired in the latter cases, use a raise statement.
https://google.github.io/styleguide/pyguide.html

NEED TO FLESH OUT P4K_CLASS TESTING BEFORE MOVING ONTO OTHER OUTLETS

> pytest -v
"""
from feeds.p4k_class import p4k


def test_p4k():
    '''Pitchfork'''
    assert isinstance(p4k, list)
