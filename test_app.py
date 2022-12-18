from app import link_dicts, link_dicts_sorted, link_dicts_sorted_and_reduced, current_date


def test_app():
    assert link_dicts
    assert link_dicts_sorted
    assert link_dicts_sorted_and_reduced
    assert current_date


'''NOTES ON PYTEST
Files must have format test_XXX.py or XXX_test.py
Test methods should start wth keyword "test"

> pytest (more details)
> pytest -q (less details)
'''
