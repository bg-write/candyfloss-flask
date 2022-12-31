from app import link_dicts, link_dicts_sorted, link_dicts_sorted_and_reduced, current_date, app


def test_app():
    assert link_dicts == link_dicts
    assert link_dicts_sorted == link_dicts_sorted
    assert link_dicts_sorted_and_reduced == link_dicts_sorted_and_reduced
    assert current_date == current_date
    assert app == app


'''NOTES ON PYTEST
Files must have format test_XXX.py or XXX_test.py
Test methods should start wth keyword "test"

> pytest (more details)
> pytest -q (less details)
'''
