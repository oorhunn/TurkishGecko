from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, StringField


class DatarefForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    coin = StringField('Coin', validators=[DataRequired()])
    interval = StringField('interval', validators=[DataRequired()])
    submit = SubmitField('Submit')




