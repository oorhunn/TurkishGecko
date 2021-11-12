def init_routes(app):

    @app.route('/health-check')
    def succes():
        return 'Dede ayakta!!!!'