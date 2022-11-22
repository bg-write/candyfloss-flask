from flask import Flask, render_template  # pip install flask
from datetime import datetime
import git  # pip install GitPython

# importing our feeds
from feeds.p4k import review_title_arr, review_URL_arr, review_author_arr, review_publication_arr

app = Flask(__name__)


@app.route('/git_update', methods=['POST'])  # webhook
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
    return render_template('hello.html', date=current_date, len=len(review_title_arr), review_title=review_title_arr, review_URL=review_URL_arr, review_author=review_author_arr, review_publication=review_publication_arr)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run

# flask --debug run
