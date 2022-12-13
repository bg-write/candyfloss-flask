from flask import Flask, render_template  # pip install flask
from datetime import datetime

# importing our feeds
from feeds.p4k import p4k
from feeds.gum import gum
from feeds.ad import ad
from feeds.ringer import ringer

# combining our feeds
link_dicts = p4k + gum + ad + ringer

# ordering our combined feed by date
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to a specific number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:50]

# Universal Time Coordinated (UTC/GMT time)
current_date = datetime.now().strftime("%b %d, %Y")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('hello.html', date=current_date, links=link_dicts_sorted_and_reduced)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

# flask --debug run
# python app.py
