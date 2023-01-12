"""

Call and clean an RSS feed and pull only the information we need.
Imports include Python's datetime, Beautiful Soup, and requests.
Can also import lxml when RSS url is not available.
"""


class Outlet:
    """

  Class summary info goes here.

  Attributes:
    title: the title
    author: the author
    publication: the publication
    url: url
    date: the date
  """

    def __init__(self, title, author, publication, url, date):
        """Inits Outlet with specified attributes."""
        self.title = title
        self.author = author
        self.publication = publication
        self.url = url
        self.date = date

    def __str__(self):
        """Returns a string representation of the object."""
        return (
            f'{self.title} ({self.author} / {self.publication}) ({self.url}) ({self.date})'
        )

    def console(self):
        """Prints to the console."""
        print(self)


# creating a new object called "pitchfork"
# using the "Outlet" class with its specified properties
pitchfork = Outlet(
    'Jumping/Dancing/Fighting EP', 'Nina Corcoran', 'Pitchfork',
    'https://pitchfork.com/reviews/albums/hammok-jumping-dancing-fighting-ep',
    '2022-12-30T05:00:00+00:00')
pitchfork.console()

# python feeds/p4k_class.py
