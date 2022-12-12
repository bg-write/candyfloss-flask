from flask import Flask, render_template  # pip install flask
from datetime import datetime
import git  # pip install GitPython

# importing our feeds
from feeds.p4k import p4k
from feeds.gum import gum
from feeds.ad import ad

# combining our feeds
link_dicts = p4k + gum + ad

# ordering our combined feed by date
link_dicts_sorted = sorted(link_dicts, key=lambda i: i['date'], reverse=True)

# reducing our feed to a specific number
link_dicts_sorted_and_reduced = link_dicts_sorted[0:20]

app = Flask(__name__)


# webhook # todo do I still need this?
@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./candyfloss-flask')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(
        origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route("/")
def hello_world():
    current_date = datetime.now().strftime("%b %d, %Y")
    return render_template('hello.html', date=current_date, links=link_dicts_sorted_and_reduced)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

# flask --debug run
# python app.py
