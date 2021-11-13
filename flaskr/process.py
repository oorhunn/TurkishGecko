import os
from flask import (
    Blueprint, render_template, session, redirect
)

from services import data_preprocess
from services.binance_service import binance_service
from services.data_preprocess import prophet_service, only_basic_pre_process
import pandas as pd
from datetime import datetime
from services.utiltyfunctions import string_to_date_refactor
from dateutil import parser


bp = Blueprint('process', __name__, url_prefix='/process')


@bp.route('/', methods=('GET', 'POST'))
def index():
    rawdata = os.listdir('coindata/rawdata/')
    prophet_data = os.listdir('coindata/preprocessed/prophetdata/')
    # not_usable_prophet_data = []
    #
    # for dat in prophet_data:
    #     month, day, year = string_to_date_refactor(dat)
    #     dateval = month + '/' + day + '/' + year
    #     local_file_date = (parser.parse(dateval)).date()
    #     today = datetime.today().date()
    #     if local_file_date != today:
    #         not_usable_prophet_data.append(dat)
    #         prophet_data.remove(dat)
    prophet_data, not_usable_prophet_data = prophet_service.check_local_data(prophet_data)

    return render_template('process/index.html', rawdata=rawdata, prophetdata=prophet_data, not_usable_prophet_data=not_usable_prophet_data)


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
    prophet_service.get_prophet_data(coin)
    return redirect('/health-check')

@bp.route('/updateprophetdata/<string:filename>')
def update_prophet_data(filename):
    temp = filename.split(' ')
    coin = temp[0]
    prophet_service.get_prophet_data(coin)
    os.remove('coindata/preprocessed/prophetdata/' + filename)
    return redirect('/process/')
