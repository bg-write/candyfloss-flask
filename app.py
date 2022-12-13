from flask import Flask, render_template  # pip install flask
from datetime import datetime

# importing our feeds
from feeds.p4k import p4k
from feeds.gum import gum
from feeds.ad import ad
from feeds.ringer import ringer
# from feeds.flux import flux
from feeds.flux_sub import flux_sub

# combining our feeds
link_dicts = p4k + gum + ad + ringer + flux_sub

# ordering our combined feed by date
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to a specific number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:50]

# Universal Time Coordinated (UTC/GMT time)
'''
https://www.geeksforgeeks.org/python-datetime-strptime-function/
WEEKDAYS
%a = Sun, Mon
%A = Sunday, Monday
%w = 0, 1
DAYS OF THE MONTH
%d = 01, 02
%-d = 1, 2
MONTHS
%b = Jan, Feb
%B = January, February
%m = 01, 02
%-m = 1, 2
YEARS
%y = 99, 00
%Y = 2000, 1999
%-y = 0, 99
HOURS
'''
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
