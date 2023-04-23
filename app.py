"""

Import feeds into one feed: sort, slice, then render.
"""
# Standard library imports
from datetime import datetime

# Third-party package imports
from flask import Flask, render_template
import sqlite3

# Local module imports (all our working feeds)
from feeds.abundant_living import abundant_living
from feeds.ad import ad
from feeds.alternative import alternative_list
# bandcamp
from feeds.billboard_chart_beat import billboard_chart_beat
# billboard global
from feeds.chi_reader import chi_reader
# creem
# eight bit theory
from feeds.flux_sub import flux_sub
# for columns
# gq
from feeds.guardian import guardian_list
from feeds.gum import gum
from feeds.loud_quiet import loud_quiet
from feeds.MJI import MJI
from feeds.nme import nme_list
from feeds.no_bells import no_bells
from feeds.no_depression import no_depression
from feeds.nyt import nyt_list
from feeds.ope import ope_list
from feeds.p4k_class import p4k
# p4k (original)
from feeds.passion_of_the_weiss import passion_of_the_weiss_list
from feeds.penny import penny
from feeds.quietus import quietus
from feeds.reply_alt import reply_alt
from feeds.ringer import ringer
# spin
from feeds.sterlewine import so_it_goes
from feeds.uproxx import uproxx
from feeds.van import van_list
# vulture
from feeds.wire import wire_list

# Combining our feeds into a list of dicts
link_dicts = (abundant_living + ad + alternative_list + billboard_chart_beat +
              chi_reader + flux_sub + guardian_list + gum + loud_quiet + MJI +
              nme_list + no_bells + no_depression + nyt_list + ope_list + p4k +
              passion_of_the_weiss_list + penny + quietus + reply_alt +
              ringer + so_it_goes + uproxx + van_list + wire_list)
'''Ordering our combined feed by date.
1) pass in our combined feed "link_dicts" to then sort.
2) Our anonymous function returns our key, which is our date.
3) Sort our feed in reverse (descending) order by our new key.
'''
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# Reducing our feed to return a specific number of links.
max_links = 50
link_dicts_sorted_and_reduced = link_dicts_sorted[0:max_links]

# Universal Time Coordinated (UTC/GMT time)
current_date = datetime.now().strftime('%b %d, %Y')


# The function connecting to our database
def get_db():
    connection = sqlite3.connect('candyfloss.db')
    connection.row_factory = sqlite3.Row
    return connection


# Define our Flask app
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Renders our main app page with our new feed and date."""
    return render_template('hello.html',
                           date=current_date,
                           links=link_dicts_sorted_and_reduced)


@app.route('/api')
def hello_api():
    """Returns our full sorted feed as an API (not sliced)."""
    return link_dicts_sorted


@app.route('/api/<outlet>')
def hello_api_outlet(outlet):
    """Returns specific outlets i.e. '/api/Pitchfork'"""
    return [
        item for item in link_dicts_sorted if item["publication"] == outlet
    ]


@app.errorhandler(404)
def page_not_found(error):
    """404 page"""
    return render_template('404.html', error=error), 404


@app.route('/db')
def hello_db():
    """Displays 'Candyfloss' db and 'feeds' table"""
    connection = get_db()
    rows = connection.execute("SELECT * FROM feeds").fetchall()
    connection.close()
    return render_template('db.html', date=current_date, rows=rows)


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
