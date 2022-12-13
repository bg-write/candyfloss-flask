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
WEEKDAYS
%a = Sun, Mon
%A = Sunday, Monday
%w = 0, 1
DAYS OF THE MONTH
%d = 01, 02
%-d = 1, 2
DAYS OF THE YEAR
%j = 001, 365
%-j = 1, 365
WEEKS OF THE YEAR
%U = 0, 6 (Sunday counts as the first day)
%W = 00, 53
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
%H = 01, 23
%-H = 1, 23
%I = 01, 12
%-I = 1, 12
%p = AM, PM
MINUTES
%M = 01, 59
%-M = 1, 59
SECONDS
%S = 01, 59
%-S = 1, 59
%f = 000000, 999999
TIME ZONES
%z = +HHMM, -HHMM
%Z = UTC
LOCALE INFO
%c = Mon Sep 30 07:06:05 2013
%x = 11/30/98
%X = 10:03:43
%% = a literal % character
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
