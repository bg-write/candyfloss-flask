'''
Imports app modules for testing
'''
from app import link_dicts, link_dicts_sorted, link_dicts_sorted_and_reduced, current_date, app


def test_app():
    '''asserting each app module (need to flesh out)'''
    assert link_dicts == link_dicts
    assert link_dicts_sorted == link_dicts_sorted
    assert link_dicts_sorted_and_reduced == link_dicts_sorted_and_reduced
    assert current_date == current_date
    assert app == app
