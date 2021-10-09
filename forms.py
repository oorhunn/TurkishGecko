from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, StringField, SelectField
import config



class DatarefForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    coin = SelectField('Coin', validators=[DataRequired()], choices=config.COIN_CHOICES)
    interval = SelectField('Interval', validators=[DataRequired()], choices=config.INTERVAL_CHOICES)
    submit = SubmitField('Submit')
