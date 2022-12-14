"""

Imports feeds into one feed, sorted and sliced and then rendered.
Imports also include Python's datetime and Flask.
"""
from datetime import datetime
from flask import Flask, render_template

# importing our feeds
from feeds.p4k import p4k
from feeds.gum import gum
from feeds.ad import ad
from feeds.ringer import ringer
from feeds.flux_sub import flux_sub
from feeds.MJI import MJI
# from feeds.creem import creem
from feeds.penny import penny
from feeds.chi_reader import chi_reader
# from feeds.vulture import vulture
from feeds.uproxx import uproxx
from feeds.quietus import quietus
# from feeds.eight_bit_theory import eight_bit_theory
from feeds.abundant_living import abundant_living
# from feeds.billboard_global import billboard_global
from feeds.billboard_chart_beat import billboard_chart_beat
# from feeds.bandcamp import bandcamp
from feeds.no_bells import no_bells
from feeds.loud_quiet import loud_quiet
from feeds.no_depression import no_depression
from feeds.sterlewine import so_it_goes
from feeds.reply_alt import reply_alt

# combining our feeds into a list of dicts
link_dicts = (p4k + gum + ad + flux_sub + MJI + penny + chi_reader + uproxx +
              abundant_living + billboard_chart_beat + ringer + no_bells +
              quietus + loud_quiet + no_depression + so_it_goes + reply_alt)

# ordering our combined feed by date
# 1) pass in our combined feed to sort (link_dicts)
# 2) our anonymous function returning our key, which is our date
# 3) sorting our feed in reverse (descending) order
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to return a specific set number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:50]

# Universal Time Coordinated (UTC/GMT time)
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
current_date = datetime.now().strftime('%b %d, %Y')

app = Flask(__name__)


@app.route('/')
def hello_world():
    """renders our main app page with our new feed and date"""
    return render_template('hello.html',
                           date=current_date,
                           links=link_dicts_sorted_and_reduced)


@app.route('/api')
def hello_api():
    """returns the full sorted feed as an API (not sliced)"""
    # TODO return specific pubs i.e. '/api/p4k' only returns Pitchfork links
    return link_dicts_sorted


@app.errorhandler(404)
def page_not_found(error):
    """404 page"""
    return render_template('404.html', error=error), 404


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

# flask --debug run
# python app.py
