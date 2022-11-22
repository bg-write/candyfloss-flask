from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    current_date = datetime.now().strftime("%b %d, %Y")
    return render_template('hello.html', date=current_date)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)