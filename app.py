from flask import Flask, render_template  # pip install flask
from datetime import datetime

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
# from feeds.quietus import quietus
# from feeds.eight_bit_theory import eight_bit_theory
from feeds.abundant_living import abundant_living
# from feeds.billboard_global import billboard_global
from feeds.billboard_chart_beat import billboard_chart_beat
from feeds.bandcamp import bandcamp
from feeds.no_bells import no_bells

# combining our feeds
link_dicts = p4k + gum + ad + flux_sub + MJI + penny + chi_reader + \
    uproxx + abundant_living + billboard_chart_beat + bandcamp + ringer + no_bells

# ordering our combined feed by date
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to return a specific set number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:50]

# Universal Time Coordinated (UTC/GMT time)
current_date = datetime.now().strftime("%b %d, %Y")

app = Flask(__name__)


@app.route("/")  # http://127.0.0.1:5000/
def hello_world():
    return render_template('hello.html', date=current_date, links=link_dicts_sorted_and_reduced)


@app.route("/api")  # http://127.0.0.1:5000/api
def hello_api():
    return link_dicts_sorted_and_reduced


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

# flask --debug run
# python app.py
