from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    pin = PasswordField("Pin", validators=[DataRequired()])
    time = DateTimeField("Time", validators=[DataRequired()])
    submit = SubmitField("Submit")
