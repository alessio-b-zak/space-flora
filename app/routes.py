import flask
import datetime as dt
from app import app
from app.forms import InputForm

@app.route("/")
@app.route("/index")
def index():
    # return "What aree yew dooeeing in maah swamph!!!"
    time = dt.datetime.now().strftime('%Y-%m-%d')
    default_user = {"username": "IwanCol"}
    form = InputForm()
    return flask.render_template("index.html", user=default_user, time=time, form=form)


@app.route("/",      methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def user_input():
    form = InputForm()
    # if form.validate_on_submit():
    flask.flash("Input requested for user {}, pin {}".format(form.username.data, form.pin.data))
    print("Success???")
    return flask.redirect("/success")
    # time = dt.datetime.now().strftime('%Y-%m-%d')
    # default_user = {"username": "IwanCol"}
    # return flask.render_template("index.html", user=default_user, time=time, form=form)
