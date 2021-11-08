from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, SelectField
from config.fe_params import COIN_CHOICES, INTERVAL_CHOICES


class DatarefForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    coin = SelectField('Coin', validators=[DataRequired()], choices=COIN_CHOICES)
    interval = SelectField('Interval', validators=[DataRequired()], choices=INTERVAL_CHOICES)
    submit = SubmitField('Submit')


class ProphetForm(FlaskForm):
    coin = SelectField('Coin', validators=[DataRequired()], choices=COIN_CHOICES)
    submit = SubmitField('Submit')