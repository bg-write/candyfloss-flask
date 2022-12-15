from p4k import p4k

# the functions we're actually testing


def feed(x):
    return x


def test_p4k():  # our testing function
    assert feed(p4k) == p4k

# python feeds/test_feeds.py

# pytest -q
# remember: fail fast!
# todo flesh out all my p4k tests, then move outward
