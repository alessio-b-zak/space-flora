import flask
import datetime as dt
from app import app
from app.forms import TimeForm

@app.route("/")
@app.route("/index")
def index():
    time = dt.datetime.now().strftime('%Y-%m-%d')
    form = TimeForm()
    return flask.render_template("index.html", time=time, form=form)


@app.route("/",      methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def user_input():
    form = TimeForm()
    time = form.time.data
    print(time)
