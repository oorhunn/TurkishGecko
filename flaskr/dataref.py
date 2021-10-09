import functools
from datetime import datetime
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import forms

bp = Blueprint('dataref', __name__, url_prefix='/dataref')


@bp.route('/', methods=('GET', 'POST'))
def dataref():
    form = forms.DatarefForm()
    if form.validate_on_submit():
        # In case of a need for clearing session data
        # session.pop('startdate')
        # session.pop('enddate')
        session['startdate'] = form.startdate.data
        session['enddate'] = form.enddate.data
        session['coin'] = form.coin.data
        session['interval'] = form.interval.data
        return redirect('check')
    return render_template('dataline/dataref.html', form=form)


@bp.route('/check', methods=('GET', 'POST'))
def check():
    checkdata = {
        'startdate ': session['startdate'],
        'enddate': session['enddate'],
        'coin': session['coin'],
        'interval': session['interval']
    }
    # startdate = session['startdate']
    # enddate = session['enddate']
    # coin = session['coin']
    # interval = session['interval']
    return render_template('dataline/check.html', data=checkdata)


