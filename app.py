from flask import Flask, render_template  # pip install flask
from datetime import datetime
import git  # pip install GitPython

# importing our feeds

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
    return render_template('hello.html', date=current_date)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

# flask run
