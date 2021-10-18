import os
from flask import (
    Blueprint, render_template, session, redirect
)

from services import data_preprocess
from services.binance_service import binance_service
from services.data_preprocess import prophet_service, only_basic_pre_process
import pandas as pd
from datetime import datetime

bp = Blueprint('process', __name__, url_prefix='/process')


@bp.route('/', methods=('GET', 'POST'))
def index():
    temp = os.listdir('coindata/rawdata/')
    return render_template('process/index.html', data=temp)


# This route separates full kline data into more simplified version
# It contains Open Time, Open, Close, High, Low and Volume data
# Then outputs into coindata/preprocessed with .csv extension
@bp.route('/basicpreprocess/<string:filename>')
def basicpreprocess(filename):
    path = 'coindata/rawdata/' + filename
    data_preprocess.basic_preprocess(path)
    return 'succes'


@bp.route('/prophetpreprocess')
def prophetpreprocess():
    coin = session['prophet coin']
    tempdata = binance_service.get_prophet_data(coin)
    daily = only_basic_pre_process(tempdata['14 Day Daily KLines'])
    fourhour = only_basic_pre_process(tempdata['7 Day 4Hour KLines'])
    onehour = only_basic_pre_process(tempdata['4 Day 1Hour KLines'])
    fiftmins = only_basic_pre_process(tempdata['2 Day 15Min KLines'])
    prophet_service.refactor_data(daily)
    prophet_service.refactor_data(fourhour)
    prophet_service.refactor_data(onehour)
    prophet_service.refactor_data(fiftmins)
    frames = [daily, fourhour, onehour, fiftmins]
    result = pd.concat(frames)
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    filename = 'coindata/preprocessed/prophetdata/' + str(coin) + ' ' + str(month) + '-' + str(day) + '-' + str(year) + '.csv'
    result.to_csv(filename)
    return redirect('/succes')
