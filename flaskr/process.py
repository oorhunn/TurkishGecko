import functools
import os
from datetime import datetime
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import forms
from os import listdir
from os.path import isfile, join
import utilfuncs


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
    utilfuncs.BasicPreprocess(path)
    return 'succes'
