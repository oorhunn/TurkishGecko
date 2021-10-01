import datetime
import json
import os
from flask import Flask, render_template, session,send_from_directory, url_for, request, redirect
from config import Config
from binance.client import Client

import forms

def create_app(config=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        # app.config.from_mapping(test_config)
        app.config.from_object(config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    error = None
    client = Client(Config.API_KEY, Config.API_SECRET)
    # res = client.get_exchange_info()
    systemstatus = client.get_system_status()
    if systemstatus['status'] != 0 and systemstatus['msg'] != 'normal':
        error = 'System is offline'

    @app.route('/succes')
    def succes():
        return 'Succes!!!!'

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
        print(session)
        # TODO remember to make time refresh with JS
        return render_template('index.html', data=generalinfo)




    # @app.route('/product_images/<filename>')
    # def upload(filename):
    #     return send_from_directory(app.config['UPLOAD_PATH'], filename)

    from . import orderinfo
    app.register_blueprint(orderinfo.bp)

    from . import dataref
    app.register_blueprint(dataref.bp)

    return app
