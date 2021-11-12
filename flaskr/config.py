import os


def init_config(app):
    print('init config')
    app.config.from_object("config.local")

    profile = os.environ.get("PYTHON_ENV")
    # if profile == "dev":
    #     app.config.from_object("config.dev")
    # elif profile == "prod":
    #     app.config.from_object("config.prod")