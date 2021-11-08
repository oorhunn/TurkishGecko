import datetime
# import os
from flask import render_template
# from flask import render_template, session, send_from_directory, url_for, request, redirect

# from binance.client import Client
# import forms
# # import io
# import random
# from flask import Response
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from services.binance_service import binance_service

from flask import Flask
from flaskr.config import init_config
from flaskr.routes import init_routes
from services.binance_service import binance_service

print('here')
app = Flask(__name__)
init_config(app)
init_routes(app)
binance_service.init_app(app)
print(app.config)


# TODO implement pandas, ta, find out how to use indicators and how to create pandas datatable
client = binance_service.get_client()
# res = client.get_exchange_info()
systemstatus = client.get_system_status()
if systemstatus['status'] != 0 and systemstatus['msg'] != 'normal':
    error = 'System is offline'

@app.route('/')
def index():
    if error is not None:
        generalinfo = error
    serverTimereq = client.get_server_time()
    serverTimeUTC = datetime.datetime.utcfromtimestamp(serverTimereq['serverTime'] / 1000)
    generalinfo={
        'Server Time UTC': serverTimeUTC,
        'System Status': systemstatus
    }
    # TODO remember to make time refresh with JS
    return render_template('index.html', data=generalinfo)


@app.route('/prophetdata')
def prophet_data():
    temp = os.listdir('coindata/preprocessed/prophetdata/')

    return render_template()

from . import orderinfo
app.register_blueprint(orderinfo.bp)

from . import dataref
app.register_blueprint(dataref.bp)

from . import process
app.register_blueprint(process.bp)
