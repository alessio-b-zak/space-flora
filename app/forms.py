from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, SubmitField
from wtforms_components import TimeField
from wtforms.validators import DataRequired

class TimeForm(FlaskForm):
    time = TimeField("Time", validators=[DataRequired()])
    submit = SubmitField("Submit")
