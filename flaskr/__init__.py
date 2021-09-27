import json
import os
from flask import Flask, render_template, send_from_directory,url_for
from config import Config
from binance.client import Client


def create_app(config=Config):
    # create and configure the app
    app = Flask(__name__)

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

    client = Client(Config.API_KEY, Config.API_SECRET)
    res = client.get_exchange_info()

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        print(client.ping())

        return 'Hello, World!'

    @app.route('/')
    def index():
        return render_template('index.html', data='yarrak')



    @app.route('/product_images/<filename>')
    def upload(filename):
        return send_from_directory(app.config['UPLOAD_PATH'], filename)

    # from . import auth
    # app.register_blueprint(auth.bp)



    return app
