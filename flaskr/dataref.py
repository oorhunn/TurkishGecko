from flask import (
    Blueprint, redirect, render_template, session
)
import forms
from services.binance_service import binance_service


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


@bp.route('/download', methods=('GET','POST'))
def download():
    interval = session['interval']
    coin = session['coin']
    startdate = session['startdate']
    binance_service.get_coin_data(coin, interval, startdate)
    return redirect('/')


@bp.route('/getprophetdata', methods=('GET','POST'))
def getprophetdata():
    form = forms.ProphetForm()
    if form.validate_on_submit():
        session['prophet coin'] = form.coin.data
        return redirect('/process/prophetpreprocess')

    return render_template('dataline/prophet.html', form=form)

