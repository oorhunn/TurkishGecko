def init_routes(app):

    @app.route('/succes')
    def succes():
        return 'Succes!!!!'