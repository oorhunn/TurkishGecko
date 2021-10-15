import functools
from datetime import datetime
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('orderinfo', __name__, url_prefix='/orderinfo')


@bp.route('/orders', methods=('GET', 'POST'))
def orders():
    # Example return for candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MONTH)
    # [
    #     [
    #         1499040000000,  # Open time
    #         "0.01634790",  # Open
    #         "0.80000000",  # High
    #         "0.01575800",  # Low
    #         "0.01577100",  # Close
    #         "148976.11427815",  # Volume
    #         1499644799999,  # Close time
    #         "2434.19055334",  # Quote asset volume
    #         308,  # Number of trades
    #         "1756.87402397",  # Taker buy base asset volume
    #         "28.46694368",  # Taker buy quote asset volume
    #         "17928899.62484339"  # Can be ignored
    #     ]
    # ]
    return 'orders end'
