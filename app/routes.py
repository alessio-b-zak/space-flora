import flask
import datetime as dt
from app import app
# import servo.py as sv
from app.forms import TimeForm

times = []

@app.route("/")
@app.route("/index")
def index():
    date = dt.datetime.now().strftime('%Y-%m-%d')
    form = TimeForm()
    return flask.render_template("index.html", time=date, times=times, form=form)


@app.route("/",      methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def user_input():
    form = TimeForm()
    time = form.time.data
    date = dt.datetime.now().strftime('%Y-%m-%d')
    print(time)
    times.append(time)
    return flask.render_template("index.html", time=date, times=times, form=form)


@app.route("/trigger")
def trigger():
    # Trigger the motor thing here
    # It'll be something like servo.idk()
    # objj = sv.App()
    # objj.rotate()
    date = dt.datetime.now().strftime('%Y-%m-%d')
    form = TimeForm()
    # return flask.render_template("index.html", time=date, form=form)
    return flask.render_template("index.html", time=date, times=times, form=form)
